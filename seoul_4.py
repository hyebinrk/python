def line4():
    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm
    import squarify
    
    
    file_path = "./서울시지하철호선별역별승하차인원정보.csv"
    df = pd.read_csv(file_path,encoding='EUC-KR')
    df['passenger'] = df['승차총승객수'] + df['하차총승객수']
    data4 = df[df['호선명']=='4호선']
    
    columns = ['date','line_name','name','b_subway','g_subway','upload','passenger']
    data4.columns = columns
    data4.loc[:'name','passenger':'passenger']
    
    data = data4.groupby(by='name').sum().reset_index()
    tdata = data[['name','passenger']]
    
    total_data = tdata.sort_values(by='passenger',ascending=False)
    total_data
    
    d2_path = "./D2Coding-Ver1.3.2-20180524.ttf"
    fm.fontManager.addfont(d2_path)
    plt.rcParams["font.family"] = "D2Coding"
    
    plt.figure(figsize=(25,7))
    squarify.plot(sizes=total_data['passenger'], label = [f"{x[0]}({x[1]}명)" for x in zip(total_data['name'],total_data['passenger'])],alpha=0.2)
    plt.rcParams['font.size'] = 10 # plt.rcParams['text.color']='blue'
    plt.gca().invert_yaxis()
    plt.axis("off")
    plt.show()

line4()
