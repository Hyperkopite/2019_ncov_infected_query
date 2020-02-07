# encoding=utf-8
import requests


def get_json(url_json):
    resp = requests.get(url_json)
    return resp.json()


if __name__ == '__main__':
    travel_type = ['飞机', '火车', '地铁', '长途客车/大巴', '公交车', '出租车', '轮船', '其他公共场所']
    url = 'http://2019ncov.nosugartech.com/data.json'
    print(u'正在联网更新数据，请稍等...')
    data = get_json(url)
    print(u'数据更新完毕。')
    for itinerary in data['data']:
        itinerary['t_type'] = travel_type[itinerary['t_type'] - 1]
    while True:
        cntr = 1
        is_found = False
        query_data = input(u'\n输入您要查询的车次/车牌/航班号/场所名/站名/地名（如需退出，按下Ctrl+C）：')
        for itinerary in data['data']:
            if str(itinerary['t_no']).lower().find(query_data.lower()) is not -1 or str(itinerary['t_pos_start']).lower().find(query_data.lower()) is not -1 or str(itinerary['t_pos_end']).lower().find(query_data.lower()) is not -1:
                print('\n---------------------------------------------------------------------------------\n' + u'|记录' + str(cntr) + '|\n\n' + u'日期：' + str(itinerary['t_date']) + '\n' + u'车次/车牌/航班号/场所名：' + str(itinerary['t_no']) + '\n' + u'出行类型：' + str(itinerary['t_type']) + '\n' + u'车厢：' + str(itinerary['t_no_sub']) + '\n' + u'出发站：' + str(itinerary['t_pos_start']) + '\n' + u'到达站：' + str(itinerary['t_pos_end']) + '\n' + u'出行描述：' + str(itinerary['t_memo']) + '\n' + u'线索来源：' + str(itinerary['source']))
                cntr += 1
                is_found = True
        if is_found is False:
            print('\n恭喜您，目前没有相关记录！\n')
        else:
            print('\n=================================================================================\n共找到' + str(cntr - 1) + '条相关记录。\n=================================================================================')
