## Ideally, they have one file with the settings for the strat and deployment
## This file would allow them to configure so they can test, deploy and interact with the strategy

BADGER_DEV_MULTISIG = "0x4977110Ed3CD5eC5598e88c8965951a47dd4e738"

WANT = "0x515e252b2b5c22b4b2b6Df66c2eBeeA871AA4d69" ## WBTC-WETH-SLP
# LP_COMPONENT = "0x8F8e95Ff4B4c5E354ccB005c6B0278492D7B5907" ## WBTC-WETH-SLP
REWARD_TOKEN = "0xd4d42F0b6DEF4CE0383636770eF773390d85c61A" ## SUSHI

PROTECTED_TOKENS = [WANT, REWARD_TOKEN] # , LP_COMPONENT
## Fees in Basis Points
DEFAULT_GOV_PERFORMANCE_FEE = 1000
DEFAULT_PERFORMANCE_FEE = 1000
DEFAULT_WITHDRAWAL_FEE = 50

FEES = [DEFAULT_GOV_PERFORMANCE_FEE, DEFAULT_PERFORMANCE_FEE, DEFAULT_WITHDRAWAL_FEE]

CONTROLLER = "0xc00e71719d1494886942d6277daea20494cf0eec"
KEEPER = "0x46fa8817624eea8052093eab8e3fdf0e2e0443b2"
GUARDIAN = "0xCD3271021e9b35EF862Dd98AFa826b8b5198826d"

