# # -*- coding: utf-8 -*-
# import os
# import time
# import json
#
#
# DOWNLOAD_PATH = os.path.join(
#     os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'download', 'Android'
# )
#
# data = {
#     'code': 10000,
#     'msg': '成功',
#     'marketList': [
#         {
#             'market_id': '6',
#             'market_name': '华为',
#             'categoryList': [
#                 {
#                     'category_id': '5',
#                     'category_name': '应用',
#                     'parent_id': '0',
#                     'subClass': [
#                         {
#                             'category_id': '5',
#                             'category_name': '影音娱乐',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '6',
#                             'category_name': '实用工具',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '7',
#                             'category_name': '社交通讯',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '8',
#                             'category_name': '教育',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '9',
#                             'category_name': '新闻阅读',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '10',
#                             'category_name': '拍摄美化',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '11',
#                             'category_name': '出行导航',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '12',
#                             'category_name': '旅游住宿',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '13',
#                             'category_name': '购物比较',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '14',
#                             'category_name': '商务',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '15',
#                             'category_name': '儿童',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '16',
#                             'category_name': '金融理财',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '17',
#                             'category_name': '运动健康',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '18',
#                             'category_name': '便捷生活',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '19',
#                             'category_name': '汽车',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '20',
#                             'category_name': '主题个性',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '21',
#                             'category_name': '美食',
#                             'parent_id': '1'
#                         }
#                     ]
#                 },
#                 {
#                     'category_id': '23',
#                     'category_name': '游戏',
#                     'parent_id': '0',
#                     'subClass': [
#                         {
#                             'category_id': '23',
#                             'category_name': '角色扮演',
#                             'parent_id': '2'
#                         },
#                         {
#                             'category_id': '24',
#                             'category_name': '休闲益智',
#                             'parent_id': '2'
#                         },
#                         {
#                             'category_id': '25',
#                             'category_name': '经营策略',
#                             'parent_id': '2'
#                         },
#                         {
#                             'category_id': '26',
#                             'category_name': '体育竞速',
#                             'parent_id': '2'
#                         },
#                         {
#                             'category_id': '27',
#                             'category_name': '棋牌桌游',
#                             'parent_id': '2'
#                         },
#                         {
#                             'category_id': '28',
#                             'category_name': '动作射击',
#                             'parent_id': '2'
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             'market_id': '4',
#             'market_name': '小米',
#             'categoryList': [
#                 {
#                     'category_id': '168',
#                     'category_name': '软件下载榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '169',
#                     'category_name': '软件飙升榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '170',
#                     'category_name': '游戏下载榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '171',
#                     'category_name': '游戏飙升榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '174',
#                     'category_name': '软件风云榜',
#                     'parent_id': '0',
#                     'subClass': [{
#                         'category_id': '174',
#                         'category_name': '全部软件',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '175',
#                         'category_name': '影音视听',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '176',
#                         'category_name': '实用工具',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '177',
#                         'category_name': '聊天社交',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '178',
#                         'category_name': '图书阅读',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '179',
#                         'category_name': '时尚购物',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '180',
#                         'category_name': '摄影摄像',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '181',
#                         'category_name': '学习教育',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '182',
#                         'category_name': '旅行交通',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '183',
#                         'category_name': '金融理财',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '184',
#                         'category_name': '娱乐消遣',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '185',
#                         'category_name': '新闻资讯',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '186',
#                         'category_name': '居家生活',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '187',
#                         'category_name': '体育运动',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '188',
#                         'category_name': '医疗健康',
#                         'parent_id': '172'
#                     }, {
#                         'category_id': '189',
#                         'category_name': '效率办公',
#                         'parent_id': '172'
#                     }]
#                 },
#                 {
#                     'category_id': '190',
#                     'category_name': '游戏风云榜',
#                     'parent_id': '0',
#                     'subClass': [
#                         {
#                             'category_id': '190',
#                             'category_name': '全部游戏',
#                             'parent_id': '173'
#                         },
#                         {
#                             'category_id': '191',
#                             'category_name': '跑酷闯关',
#                             'parent_id': '173'
#                         },
#                         {
#                             'category_id': '192',
#                             'category_name': '网游RPG',
#                             'parent_id': '173'
#                         },
#                         {
#                             'category_id': '193',
#                             'category_name': '赛车体育',
#                             'parent_id': '173'
#                         },
#                         {
#                             'category_id': '194',
#                             'category_name': '飞行空战',
#                             'parent_id': '173'
#                         },
#                         {
#                             'category_id': '195',
#                             'category_name': '动作枪战',
#                             'parent_id': '173'
#                         },
#                         {
#                             'category_id': '196',
#                             'category_name': '格斗快打',
#                             'parent_id': '173'
#                         },
#                         {
#                             'category_id': '197',
#                             'category_name': '休闲创意',
#                             'parent_id': '173'
#                         },
#                         {
#                             'category_id': '198',
#                             'category_name': '棋牌桌游',
#                             'parent_id': '173'
#                         },
#                         {
#                             'category_id': '199',
#                             'category_name': '模拟经营',
#                             'parent_id': '173'
#                         },
#                         {
#                             'category_id': '200',
#                             'category_name': '战争策略',
#                             'parent_id': '173'
#                         },
#                         {
#                             'category_id': '201',
#                             'category_name': '塔防迷宫',
#                             'parent_id': '173'
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             'market_id': '8',
#             'market_name': 'VIVO',
#             'categoryList': [
#                 {
#                     'category_id': '4',
#                     'category_name': '应用榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '5',
#                     'category_name': '单机榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '6',
#                     'category_name': '网游榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '7',
#                     'category_name': '热搜榜',
#                     'parent_id': '0'
#                 }
#             ]
#         },
#         {
#             'market_id': '9',
#             'market_name': 'OPPO',
#             'categoryList': [
#                 {
#                     'category_id': '5',
#                     'category_name': '软件榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '6',
#                     'category_name': '游戏榜',
#                     'parent_id': '0'
#                 }
#             ]
#         },
#         {
#             'market_id': '7',
#             'market_name': '魅族',
#             'categoryList': [
#                 {
#                     'category_id': '4',
#                     'category_name': '排行',
#                     'parent_id': '0',
#                     'subClass': [
#                         {
#                             'category_id': '4',
#                             'category_name': '热门榜',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '6',
#                             'category_name': '飙升榜',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '7',
#                             'category_name': '新品榜',
#                             'parent_id': '1'
#                         },
#                         {
#                             'category_id': '159',
#                             'category_name': '游戏榜',
#                             'parent_id': '1'
#                         }
#                     ]
#                 },
#                 {
#                     'category_id': '5',
#                     'category_name': '游戏',
#                     'parent_id': '0',
#                     'subClass': [
#                         {
#                             'category_id': '5',
#                             'category_name': '畅销榜',
#                             'parent_id': '3'
#                         },
#                         {
#                             'category_id': '173',
#                             'category_name': '热门榜',
#                             'parent_id': '3'
#                         },
#                         {
#                             'category_id': '174',
#                             'category_name': '新游榜',
#                             'parent_id': '3'
#                         },
#                         {
#                             'category_id': '175',
#                             'category_name': '免费榜',
#                             'parent_id': '3'
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             'market_id': '3',
#             'market_name': '应用宝',
#             'categoryList': [
#                 {
#                     'category_id': '154',
#                     'category_name': '流行榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '155',
#                     'category_name': '新品榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '156',
#                     'category_name': '热销榜',
#                     'parent_id': '0'
#                 }
#             ]
#         },
#         {
#             'market_id': '2',
#             'market_name': '百度',
#             'categoryList': [
#                 {
#                     'category_id': '198',
#                     'category_name': '游戏',
#                     'parent_id': '0',
#                     'subClass': [
#                         {
#                             'category_id': '198',
#                             'category_name': '热搜榜',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '199',
#                             'category_name': '飙升榜',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '200',
#                             'category_name': '新游榜',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '201',
#                             'category_name': '单机榜',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '202',
#                             'category_name': '网游榜',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '203',
#                             'category_name': '精品榜',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '204',
#                             'category_name': '预约榜',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '205',
#                             'category_name': '休闲',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '206',
#                             'category_name': '跑酷',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '207',
#                             'category_name': 'MOBA',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '208',
#                             'category_name': '角色扮演',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '209',
#                             'category_name': '棋牌',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '210',
#                             'category_name': '赛车',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '211',
#                             'category_name': '射击',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '212',
#                             'category_name': '养成',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '213',
#                             'category_name': '塔防',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '214',
#                             'category_name': '消除',
#                             'parent_id': '196'
#                         },
#                         {
#                             'category_id': '215',
#                             'category_name': '解密逃脱',
#                             'parent_id': '196'
#                         }
#                     ]
#                 },
#                 {
#                     'category_id': '216',
#                     'category_name': '软件',
#                     'parent_id': '0',
#                     'subClass': [
#                         {
#                             'category_id': '216',
#                             'category_name': '热搜榜',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '217',
#                             'category_name': '飙升榜',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '218',
#                             'category_name': '新锐榜',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '219',
#                             'category_name': '视频',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '220',
#                             'category_name': '音乐',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '221',
#                             'category_name': '社交',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '222',
#                             'category_name': '电子书',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '223',
#                             'category_name': '直播',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '224',
#                             'category_name': '漫画',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '225',
#                             'category_name': '购物',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '226',
#                             'category_name': '新闻',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '227',
#                             'category_name': '拍照',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '228',
#                             'category_name': '短视频',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '229',
#                             'category_name': '辅导',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '230',
#                             'category_name': '儿童',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '231',
#                             'category_name': '理财',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '232',
#                             'category_name': '旅游',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '233',
#                             'category_name': '出行',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '234',
#                             'category_name': '母婴',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '235',
#                             'category_name': '健康',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '236',
#                             'category_name': '办公',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '237',
#                             'category_name': '工具',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '238',
#                             'category_name': '手机管理',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '239',
#                             'category_name': '求职',
#                             'parent_id': '197'
#                         },
#                         {
#                             'category_id': '240',
#                             'category_name': '美化',
#                             'parent_id': '197'
#                         }
#                     ]
#                 }
#             ]
#         },
#         {
#             'market_id': '1',
#             'market_name': '360',
#             'categoryList': [
#                 {
#                     'category_id': '706',
#                     'category_name': '飙升榜',
#                     'parent_id': '700'
#                 },
#                 {
#                     'category_id': '707',
#                     'category_name': '热搜榜',
#                     'parent_id': '700'
#                 },
#                 {
#                     'category_id': '708',
#                     'category_name': '新锐榜',
#                     'parent_id': '700'
#                 },
#                 {
#                     'category_id': '709',
#                     'category_name': '月总榜',
#                     'parent_id': '700'
#                 }
#             ]
#         },
#         {
#             'market_id': '5',
#             'market_name': '豌豆荚',
#             'categoryList': [
#                 {
#                     'category_id': '176',
#                     'category_name': '软件下载榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '177',
#                     'category_name': '游戏下载榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '178',
#                     'category_name': '专业榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '179',
#                     'category_name': '飙升榜',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '180',
#                     'category_name': '新游榜',
#                     'parent_id': '0'
#                 }
#             ]
#         },
#         {
#             'market_id': '10',
#             'market_name': 'Google Play(美国)',
#             'is_show_country': False,
#             'collectionList': {
#                 'cn': [
#                     {
#                         'collection_id': '7',
#                         'collection_name': '热门免费',
#                         'collection_ename': 'apps_topselling_free'
#                     },
#                     {
#                         'collection_id': '8',
#                         'collection_name': '创收最高',
#                         'collection_ename': 'apps_topgrossing'
#                     },
#                     {
#                         'collection_id': '9',
#                         'collection_name': '上升最快',
#                         'collection_ename': 'apps_movers_shakers'
#                     },
#                     {
#                         'collection_id': '10',
#                         'collection_name': '热门付费',
#                         'collection_ename': 'apps_topselling_paid'
#                     }
#                 ],
#                 'us': [
#                     {
#                         'collection_id': '7',
#                         'collection_name': '热门免费',
#                         'collection_ename': 'apps_topselling_free'
#                     },
#                     {
#                         'collection_id': '8',
#                         'collection_name': '创收最高',
#                         'collection_ename': 'apps_topgrossing'
#                     },
#                     {
#                         'collection_id': '9',
#                         'collection_name': '上升最快',
#                         'collection_ename': 'apps_movers_shakers'
#                     },
#                     {
#                         'collection_id': '10',
#                         'collection_name': '热门付费',
#                         'collection_ename': 'apps_topselling_paid'
#                     }
#                 ]
#             },
#             'categoryList': [
#                 {
#                     'category_id': '1',
#                     'category_name': '应用',
#                     'parent_id': '0'
#                 },
#                 {
#                     'category_id': '35',
#                     'category_name': '游戏',
#                     'parent_id': '0'
#                 }
#             ]
#         }
#     ]
# }
#
# market_list = data.get('marketList')
# markets = []
#
# for market in market_list:
#     market_id = market.get('market_id')
#     market_name = market.get('market_name')
#     if market.get('categoryList'):
#         for category in market['categoryList']:
#             category_id = category.get('category_id')
#             category_name = category.get('category_name')
#             markets.append(
#                 {
#                     'market_id': market_id,
#                     'market_name': market_name,
#                     'category_id': category_id,
#                     'category_name': category_name
#                 }
#             )
#             if category.get('subClass'):
#                 for sub in category['subClass']:
#                     sub_category_id = sub.get('category_id')
#                     sub_category_name = sub.get('category_name')
#                     markets.append(
#                         {
#                             'market_id': market_id,
#                             'market_name': market_name,
#                             'category_id': sub_category_id,
#                             'category_name': sub_category_name
#                         }
#                     )
#
# # with open('market_list.json', 'w') as fp:
# #     fp.write(json.dumps(markets, ensure_ascii=False, indent=4))
#
#
# # 目录初始化
# for market in markets:
#     DATE_PATH = os.path.join(DOWNLOAD_PATH, time.strftime('%Y-%m-%d', time.localtime()))
#     if not os.path.exists(DATE_PATH):
#         os.mkdir(DATE_PATH)
#
#     MARKET_PATH = os.path.join(DATE_PATH, market['market_name'])
#     if not os.path.exists(MARKET_PATH):
#         os.mkdir(MARKET_PATH)
#
#     CATEGORY_PATH = os.path.join(MARKET_PATH, market['category_name'])
#     if not os.path.exists(CATEGORY_PATH):
#         os.mkdir(CATEGORY_PATH)
#
#