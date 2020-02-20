# coding=utf-8
import requests
import time

travel_type = [u'飞机', u'火车', u'地铁', u'长途客车/大巴', u'公交车', u'出租车', u'轮船', u'其他公共场所']
url = 'http://2019ncov.nosugartech.com/data.json'
latest_time = ''
cntr = 1
is_found = False


def get_json(url_json):
    resp = requests.get(url_json)
    return resp.json()


def print_res():
    global cntr, is_found
    print('\n---------------------------------------------------------------------------------\n' + u'|记录' + str(cntr) + '|\n\n' + u'日期：' + str(itinerary['t_date']) + '\n' + u'车次/车牌/航班号/场所名：' + str(itinerary['t_no']) + '\n' + u'出行类型：' + str(itinerary['t_type']) + '\n' + u'车厢：' + str(itinerary['t_no_sub']) + '\n' + u'出发站：' + str(itinerary['t_pos_start']) + '\n' + u'到达站：' + str(itinerary['t_pos_end']) + '\n' + u'出行描述：' + str(itinerary['t_memo']) + '\n' + u'线索来源：' + str(itinerary['source']))
    cntr += 1
    is_found = True


if __name__ == '__main__':
    print(u'[!] 正在联网更新数据，请稍等...')
    data = get_json(url)
    for itinerary in data['data']:
        latest_time = max(latest_time, itinerary['updated_at'])
        itinerary['t_type'] = travel_type[itinerary['t_type'] - 1]
    print(u'[+] 数据更新完毕。')
    time.sleep(0.5)
    print('[+] 当前共有' + str(len(data['data'])) + u'条数据。数据更新时间：' + str(latest_time))

    while True:
        cntr = 1
        is_found = False
        query_data = input(u'\n[?] 输入您要查询的车次/车牌/航班号/场所名/站名/地名/时间（时间格式：yyyy-mm-dd/mm-dd；如需退出，按下Ctrl+C）：')
        for itinerary in data['data']:
            if query_data.find('-') is not -1:
                if str(itinerary['t_date']).find(query_data) is not -1:
                    print_res()
            elif str(itinerary['t_no']).lower().find(query_data.lower()) is not -1 or str(itinerary['t_pos_start']).lower().find(query_data.lower()) is not -1 or str(itinerary['t_pos_end']).lower().find(query_data.lower()) is not -1:
                print_res()
        if is_found is False:
            print(u'\n[V] 恭喜您，目前没有相关记录！\n')
        else:
            print(u'\n---------------------------------------------------------------------------------\n共找到' + str(cntr - 1) + u'条相关记录。\n'u'=================================================================================\n')
