import time
from api.filfox import getMInerReward
from api.lotus_service import state_miner_power, initial_state_miner_info, wallet_balance, \
    state_miner_available_balance, state_miner_sector_count, read_state
import logging
import logging.config

# create logger
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

BYTE_TO_TB = 1024 ** 4
DAY_SECOND = 24 * 3600
NANOFIL_TO_FIL = 1000000000 ** 2
if __name__ == '__main__':
    miner_id = 'f02387'
    miner_reward_block = getMInerReward(miner_id)

    current_period_reward = 0
    total_winCount = 0
    accumulate_unlock_reward = 0
    current_time = int(time.time())
    total_released_to_day = 0
    today_release = 0

    logger.info('miner id:' + miner_id)
    state_miner_power_ = state_miner_power(miner_id)
    miner_info_ = initial_state_miner_info(miner_id)
    owner_addr = wallet_balance(miner_info_["result"]["Owner"])
    owner_balance = float(owner_addr['result'])
    worker_addr = wallet_balance(miner_info_["result"]["Worker"])
    worker_balance = float(worker_addr['result'])
    control_balance = 0
    control_addresses_ = miner_info_["result"]["ControlAddresses"]
    for addr in control_addresses_:
        control_balance += float(wallet_balance(addr)['result'])
    state_miner_available_balance_ = state_miner_available_balance(miner_id)
    node_balance = float(wallet_balance(miner_id)['result'])
    state_miner_sector_count_ = state_miner_sector_count(miner_id)

    raw_power = float(state_miner_power_['result']['MinerPower']['RawBytePower']) / BYTE_TO_TB
    adjusted_power = float(state_miner_power_['result']['MinerPower']['QualityAdjPower']) / BYTE_TO_TB
    operator_balance = 0.0
    if owner_addr == worker_addr:
        if owner_addr in control_addresses_:
            operator_balance = control_balance
        else:
            operator_balance = control_balance + worker_balance
    elif worker_addr in control_addresses_:
        operator_balance = owner_balance + control_balance
    elif owner_balance in control_addresses_:
        operator_balance = worker_balance + control_balance
    else:
        operator_balance = owner_balance + worker_balance + control_balance

    address_balance = (node_balance + operator_balance) / NANOFIL_TO_FIL
    available_balance = float(state_miner_available_balance_['result']) / NANOFIL_TO_FIL
    sector_active = int(state_miner_sector_count_['result']['Active'])
    sector_total = int(state_miner_sector_count_['result']['Live'])
    sector_faults = int(state_miner_sector_count_['result']['Faulty'])
    logger.info("address_balance %f，avaliable balance :%f" % (address_balance, available_balance))

    node_vesting = int(read_state(miner_id)['result']['State']['LockedFunds']) / NANOFIL_TO_FIL
    for block in miner_reward_block:
        reward = int(block['reward']) / (10.0 ** 18)
        cid = block['cid']
        height = block['height']
        winCount = block['winCount']
        block_timestamp = float(block['timestamp'])
        current_period_reward += reward
        unlock_reward = reward * 0.25
        second_reward = reward * 0.75 / (179 * DAY_SECOND)
        accumulate_unlock_reward += unlock_reward
        total_winCount += winCount
        released_time = current_time - block_timestamp
        today_release += second_reward * DAY_SECOND
        print("Reward block height：%s accumulate unlock reward： %f,Unlocked Days %f " % (height, second_reward * released_time, released_time / DAY_SECOND))
        total_released_to_day += second_reward * released_time
    vesting_balance = current_period_reward - accumulate_unlock_reward - total_released_to_day
    logger.info(' Node Number  %s : Blocks: %d  Total Reward : %f  accumulate unlock reward: %f ，Total unlock reward%f \n locked Reward%f Node locked %f，difference %f Today Estimation %f' % (
        miner_id, total_winCount, current_period_reward, accumulate_unlock_reward, total_released_to_day,
        vesting_balance, node_vesting, node_vesting-vesting_balance , today_release))
