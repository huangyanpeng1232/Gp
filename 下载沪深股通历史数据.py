import requests
import json

token = '894050c76af8597a853f5b408b759f5d'

def getHistoryData(type):
    url = 'https://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?st=DetailDate&sr=-1&ps=999999&p=1&type' \
          '=HSGTHIS&token='+token+'&filter=(MarketType=' + str(type) + ') '
    gts = requests.get(url)
    gts = gts.json()

    array = []
    for gt in gts:
        array.append({
            "日期": gt["DetailDate"],
            "当日成交净买额": str(round(gt["DRCJJME"] / 100, 2))+'亿',
            "买入成交额": str(round(gt["MRCJE"] / 100, 2))+'亿',
            "卖出成交额": str(round(gt["MCCJE"] / 100, 2))+'亿',
            "历史累计净买额": str(round(gt["LSZJLR"] / 100, 2))+'亿',
            "当日资金流入": str(round(gt["DRZJLR"] / 100, 2))+'亿',
            "当日余额": str(round(gt["DRYE"] / 100, 2))+'亿',
            "领涨股": gt["LCG"],
            "领涨股涨跌幅": str(round(gt["LCGZDF"], 2)) + '%',
            "上证指数": round(gt["SSEChange"], 2),
            "涨跌幅": str(round(gt["SSEChangePrecent"] * 100, 2)) + '%'
        })
    return array


def initData():
    hgtArray = getHistoryData('1')
    sgtArray = getHistoryData('3')

    with open("沪股通历史数据.json", "w", encoding='utf-8') as f:
        json.dump(hgtArray, f, ensure_ascii=False)
        print("沪股通历史数据 " + str(len(hgtArray)) + ' 条已保存至文件')

    with open("深股通历史数据.json", "w", encoding='utf-8') as f:
        json.dump(sgtArray, f, ensure_ascii=False)
        print("深股通历史数据 " + str(len(sgtArray)) + ' 条已保存至文件')

initData()