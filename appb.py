import streamlit as st
import pandas as pd
import re

#定义面板输入函数
def mb_shuru(shuxing):
    if shuxing == "":
        return 0
    else:
        # 验证输入只包含合法的字符（数字、运算符、小数点、括号等）
        if re.match(r'^[\d\+\-\*/\.\(\)\s]+$', shuxing):
            try:
                # 安全执行输入的数学表达式
                shuxing = eval(shuxing)
            except:
                # 如果输入的表达式有误，返回0
                st.warning("输入的表达式有误，请检查后重新输入。否则此值不生效")
                shuxing = 0
        else:
            # 如果包含非法字符，返回0
            st.warning("输入包含非法字符，请检查是否是英文的括号和乘除法*/，然后重新输入。否则此值不生效")
            shuxing = 0
    return shuxing

#定义百分比输入函数
def bfb_shuru(baifenbi):
    if baifenbi == "":
        return 0
    else:
        # 验证输入只包含合法的字符
        if re.match(r'^[\d\+\-\*/\.\(\)\s]+$', baifenbi):
            try:
                # 计算百分比并返回
                baifenbi = eval(baifenbi) * 0.01
            except:
                baifenbi = 0
                st.warning("输入的表达式有误，请检查后重新输入。否则此值不生效")
        else:
            baifenbi = 0
            st.warning("输入包含非法字符，请检查是否是英文的括号和乘除法*/，然后重新输入。否则此值不生效")
    return baifenbi

# 定义将百分比字符串转化为数值（浮动小数）的函数
def convert_percentage_to_float(percentage_str):
    return float(percentage_str.strip('%')) / 100

#标题
st.title('梦幻模拟战-面板模拟计算器')

# 定义侧边栏选项
SIDEBAR_OPTIONS = ["英雄面板模拟", "士兵面板模拟", "神契设置"]

# 获取侧边栏选项并设置默认值
selection = st.sidebar.radio("导航栏", SIDEBAR_OPTIONS, index=0, key="sidebar")

# 初始化变量
if 'bz' not in st.session_state:
    st.session_state.bz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化白字 字典
if 'lz' not in st.session_state:
    st.session_state.lz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化绿字 字典
if 'zw' not in st.session_state:
    st.session_state.zw = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化铸纹加成 字典
if 'zyjt' not in st.session_state:
    st.session_state.zyjt = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化职业精通 字典
if 'jjjt' not in st.session_state:
    st.session_state.jjjt = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化竞技精通 字典
if 'wqfm_bfb' not in st.session_state:
    st.session_state.wqfm_bfb = {"生命":"0%","攻击":"0%","智力":"0%","防御":"0%","魔防":"0%"}  # 初始化武器附魔百分比 字典
if 'yffm_bfb' not in st.session_state:
    st.session_state.yffm_bfb = {"生命":"0%","攻击":"0%","智力":"0%","防御":"0%","魔防":"0%"}  # 初始化衣服附魔百分比 字典
if 'tsfm_bfb' not in st.session_state:
    st.session_state.tsfm_bfb = {"生命":"0%","攻击":"0%","智力":"0%","防御":"0%","魔防":"0%"}  # 初始化头饰附魔百分比 字典
if 'spfm_bfb' not in st.session_state:
    st.session_state.spfm_bfb = {"生命":"0%","攻击":"0%","智力":"0%","防御":"0%","魔防":"0%"}  # 初始化饰品附魔百分比 字典
if 'gmfm_bfb' not in st.session_state:
    st.session_state.gmfm_bfb = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}  # 初始化共鸣附魔百分比 字典
if 'fm_bfb' not in st.session_state:
    st.session_state.fm_bfb = {"生命":"0%","攻击":"0%","智力":"0%","防御":"0%","魔防":"0%"}  # 初始化附魔总百分比 字典
if 'wqfm_gdz' not in st.session_state:
    st.session_state.wqfm_gdz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}  # 初始化武器附魔固定值 字典
if 'yffm_gdz' not in st.session_state:
    st.session_state.yffm_gdz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}  # 初始化衣服附魔固定值 字典
if 'tsfm_gdz' not in st.session_state:
    st.session_state.tsfm_gdz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}  # 初始化头饰附魔固定值 字典
if 'spfm_gdz' not in st.session_state:
    st.session_state.spfm_gdz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}  # 初始化饰品附魔固定值 字典
if 'fm_gdz' not in st.session_state:
    st.session_state.fm_gdz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}  # 初始化附魔总固定值 字典

if 'wq_jc' not in st.session_state:
    st.session_state.wq_jc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化武器基础值 字典
if 'yf_jc' not in st.session_state:
    st.session_state.yf_jc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化衣服基础值 字典
if 'ts_jc' not in st.session_state:
    st.session_state.ts_jc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化头饰基础值 字典
if 'sp_jc' not in st.session_state:
    st.session_state.ts_jc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化饰品基础值 字典
if 'zb_jc' not in st.session_state:
    st.session_state.zb_jc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化装备基础值总加成 字典

if 'sq_slsb' not in st.session_state:
    st.session_state.sq_slsb = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0,"士兵生命":0,"士兵攻击":0,"士兵防御":0,"士兵魔防":0}  # 初始化神契神力石板加成 字典
if 'sq_cxzz' not in st.session_state:
    st.session_state.sq_cxzz = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0,"士兵生命":0,"士兵攻击":0,"士兵防御":0,"士兵魔防":0}  # 初始化神契晨曦之祝加成 字典
if 'sq_cxzz_sbgd' not in st.session_state:
    st.session_state.sq_cxzz_sbgd = {"士兵生命":"0","士兵攻击":"0","士兵防御":"0","士兵魔防":"0"}  # 过渡 字典 存用户选择的士兵加成百分比
if 'sq_zjc' not in st.session_state:
    st.session_state.sq_zjc = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0,"士兵生命":0,"士兵攻击":0,"士兵防御":0,"士兵魔防":0}  # 初始化神契总加成 字典

# 初始化附魔选取的列表
wq_sm_bfb_percentages10 = ["10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
wq_gj_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
wq_zl_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
wq_fy_bfb_percentages5 = ["5%","4%","3%","2%","1%","0%"]
wq_mf_bfb_percentages5 = ["5%","4%","3%","2%","1%","0%"]

yf_sm_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
yf_gj_bfb_percentages5 = ["5%","4%","3%","2%","1%","0%"]
yf_zl_bfb_percentages5 = ["5%","4%","3%","2%","1%","0%"]
yf_fy_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
yf_mf_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]

ts_sm_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
ts_gj_bfb_percentages5 = ["5%","4%","3%","2%","1%","0%"]
ts_zl_bfb_percentages5 = ["5%","4%","3%","2%","1%","0%"]
ts_fy_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
ts_mf_bfb_percentages15 = ["15%","14%","13%","12%","11%","10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]

sp_sm_bfb_percentages10 = ["10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
sp_gj_bfb_percentages10 = ["10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
sp_zl_bfb_percentages10 = ["10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
sp_fy_bfb_percentages10 = ["10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]
sp_mf_bfb_percentages10 = ["10%","9%","8%","7%","6%","5%","4%","3%","2%","1%","0%"]

wq_sm_gdz_numbers130 = list(range(0, 131))
wq_gj_gdz_numbers30 = list(range(0, 31))
wq_zl_gdz_numbers30 = list(range(0, 31))
wq_fy_gdz_numbers6 = list(range(0, 7))
wq_mf_gdz_numbers6 = list(range(0, 7))

yf_sm_gdz_numbers200 = list(range(0, 201))
yf_gj_gdz_numbers10 = list(range(0, 11))
yf_zl_gdz_numbers10 = list(range(0, 11))
yf_fy_gdz_numbers18 = list(range(0, 19))
yf_mf_gdz_numbers18 = list(range(0, 19))

ts_sm_gdz_numbers200 = list(range(0, 201))
ts_gj_gdz_numbers10 = list(range(0, 11))
ts_zl_gdz_numbers10 = list(range(0, 11))
ts_fy_gdz_numbers18 = list(range(0, 19))
ts_mf_gdz_numbers18 = list(range(0, 19))

sp_sm_gdz_numbers130 = list(range(0, 131))
sp_gj_gdz_numbers20 = list(range(0, 21))
sp_zl_gdz_numbers20 = list(range(0, 21))
sp_fy_gdz_numbers12 = list(range(0, 13))
sp_mf_gdz_numbers12 = list(range(0, 13))

# 根据选项显示不同的内容
if selection == "英雄面板模拟":
    st.write("### 英雄面板计算结果")
    if st.button("点击刷新计算结果"):
        st.markdown(f"#### 生命: {st.session_state.bz["生命"]} <strong><span style='color:green;font-size:25px;'> + {st.session_state.lz["生命"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 攻击: {st.session_state.bz["攻击"]} <strong><span style='color:green;font-size:25px;'> + {st.session_state.lz["攻击"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 智力: {st.session_state.bz["智力"]} <strong><span style='color:green;font-size:25px;'> + {st.session_state.lz["智力"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 防御: {st.session_state.bz["防御"]} <strong><span style='color:green;font-size:25px;'> + {st.session_state.lz["防御"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 魔防: {st.session_state.bz["魔防"]} <strong><span style='color:green;font-size:25px;'> + {st.session_state.lz["魔防"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 技巧: {st.session_state.bz["技巧"]} <strong><span style='color:green;font-size:25px;'> + {st.session_state.lz["技巧"]}</span></strong>",unsafe_allow_html=True)

    # 分割线
    st.divider()

    st.write("### 英雄白字区")

    @st.cache_data  # 缓存数据，避免重复读取文件
    def load_data(file_path):
        df = pd.read_csv(file_path)  # 读取CSV文件
        return df
    # 加载数据
    csv_file_path = './data/梦战英雄白字.csv'  # 替换为实际文件路径
    df1 = load_data(csv_file_path)

    # 英雄选择
    hero_names = df1['英雄名'].unique()
    selected_hero = st.selectbox("请选择英雄名", hero_names)

    # 根据选中英雄，获取其所有职业
    hero_jobs = df1[df1['英雄名'] == selected_hero]['职业名']
    selected_job = st.selectbox("请选择职业", hero_jobs)

    if selected_hero == "自定义英雄":
        st.session_state.bz["生命"] = st.number_input("生命-白字", value=st.session_state.bz["生命"])  # 生命白字
        st.session_state.bz["攻击"] = st.number_input("攻击-白字", value=st.session_state.bz["攻击"])  # 攻击白字
        st.session_state.bz["智力"] = st.number_input("智力-白字", value=st.session_state.bz["智力"])  # 智力白字
        st.session_state.bz["防御"] = st.number_input("防御-白字", value=st.session_state.bz["防御"])  # 防御白字
        st.session_state.bz["魔防"] = st.number_input("魔防-白字", value=st.session_state.bz["魔防"])  # 魔防白字
        st.session_state.bz["技巧"] = st.number_input("技巧-白字", value=st.session_state.bz["技巧"])  # 技巧白字
    else:
        # 根据选择的英雄和职业，获取属性值
        selected_row = df1[(df1['英雄名'] == selected_hero) & (df1['职业名'] == selected_job)].iloc[0]
        st.session_state.bz = {
            "生命": selected_row["生命"],
            "攻击": selected_row["攻击"],
            "智力": selected_row["智力"],
            "防御": selected_row["防御"],
            "魔防": selected_row["魔防"],
            "技巧": selected_row["技巧"],
        }
        st.markdown(f"#### 生命: {st.session_state.bz["生命"]}")
        st.markdown(f"#### 攻击: {st.session_state.bz["攻击"]}")
        st.markdown(f"#### 智力: {st.session_state.bz["智力"]}")
        st.markdown(f"#### 防御: {st.session_state.bz["防御"]}")
        st.markdown(f"#### 魔防: {st.session_state.bz["魔防"]}")
        st.markdown(f"#### 技巧: {st.session_state.bz["技巧"]}")

    # 分割线
    st.divider()

    st.write("### 英雄绿字区")

    tab1,tab2,tab3,tab4,tab5,tab6 = st.tabs(["装备","附魔","职业精通","铸纹","神契","绿字总加成"])
    with tab1:
        column11, column12, column13 = st.columns([1, 0.1, 0.5])
        with column11:
            # 读取 装备基础属性CSV 文件
            file_path = "./data/梦战装备满级基础属性分类.csv"  # 读取CSV文件路径
            df2 = load_data(file_path)

            # 将数据转换为字典，按“名称”索引
            zb_dict = df2.set_index("装备名称").T.to_dict()

            # 筛选数据，根据类型生成选择框
            wq_options = df2[df2["类别"] == "武器"]["装备名称"].tolist()
            yf_options = df2[df2["类别"] == "衣服"]["装备名称"].tolist()
            ts_options = df2[df2["类别"] == "头饰"]["装备名称"].tolist()
            sp_options = df2[df2["类别"] == "饰品"]["装备名称"].tolist()

            # 用户选择框
            st.session_state.yx_wq = st.selectbox("请选择武器", wq_options)
            if st.session_state.yx_wq and st.session_state.yx_wq in zb_dict:
                st.session_state.wq_jc = zb_dict[st.session_state.yx_wq]
                st.markdown(f"武器代表:<span style='color:orange;font-size:16px;'> {zb_dict[st.session_state.yx_wq]['代表']}</span>",unsafe_allow_html=True)  # 显示武器的代表

            st.session_state.yx_yf = st.selectbox("请选择衣服", yf_options)
            if st.session_state.yx_yf and st.session_state.yx_yf in zb_dict:
                st.session_state.yf_jc = zb_dict[st.session_state.yx_yf]
                st.markdown(f"衣服代表:<span style='color:orange;font-size:16px;'>{zb_dict[st.session_state.yx_yf]['代表']}</span>",unsafe_allow_html=True)  # 显示衣服的代表

            st.session_state.yx_ts = st.selectbox("请选择头饰", ts_options)
            if st.session_state.yx_ts and st.session_state.yx_ts in zb_dict:
                st.session_state.ts_jc = zb_dict[st.session_state.yx_ts]
                st.markdown(f"头饰代表:<span style='color:orange;font-size:16px;'> {zb_dict[st.session_state.yx_ts]['代表']}</span>",unsafe_allow_html=True)  # 显示头饰的代表

            st.session_state.yx_sp = st.selectbox("请选择饰品", sp_options)
            if st.session_state.yx_sp and st.session_state.yx_sp in zb_dict:
                st.session_state.sp_jc = zb_dict[st.session_state.yx_sp]
                st.markdown(f"饰品代表:<span style='color:orange;font-size:16px;'> {zb_dict[st.session_state.yx_sp]['代表']}</span>",unsafe_allow_html=True)  # 显示饰品的代表

        with column13:
            # 相加各部分基础值
            st.session_state.zb_jc["生命"] = st.session_state.wq_jc["生命"] + st.session_state.yf_jc["生命"] + st.session_state.ts_jc["生命"] +st.session_state.sp_jc["生命"]
            st.session_state.zb_jc["攻击"] = st.session_state.wq_jc["攻击"] + st.session_state.yf_jc["攻击"] + st.session_state.ts_jc["攻击"] +st.session_state.sp_jc["攻击"]
            st.session_state.zb_jc["智力"] = st.session_state.wq_jc["智力"] + st.session_state.yf_jc["智力"] + st.session_state.ts_jc["智力"] +st.session_state.sp_jc["智力"]
            st.session_state.zb_jc["防御"] = st.session_state.wq_jc["防御"] + st.session_state.yf_jc["防御"] + st.session_state.ts_jc["防御"] +st.session_state.sp_jc["防御"]
            st.session_state.zb_jc["魔防"] = st.session_state.wq_jc["魔防"] + st.session_state.yf_jc["魔防"] + st.session_state.ts_jc["魔防"] +st.session_state.sp_jc["魔防"]
            st.session_state.zb_jc["技巧"] = st.session_state.wq_jc["技巧"] + st.session_state.yf_jc["技巧"] + st.session_state.ts_jc["技巧"] +st.session_state.sp_jc["技巧"]

            # 显示装备基础绿字总加成
            st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zb_jc["生命"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zb_jc["攻击"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zb_jc["智力"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zb_jc["防御"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zb_jc["魔防"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zb_jc["技巧"]}</span></strong>",unsafe_allow_html=True)

    with tab2:
        column21,column211,column22,column221,column23 = st.columns([1,0.1,1,0.1,1])
        with column21:

            gm_fm_1 = st.selectbox("第一个共鸣2件套", ("无","满月","轻风","时钟","怒涛","魔术","顽石","水晶","寒冰","流星","烈日","大树","荆棘","钢铁"))
            gm_fm_2 = st.selectbox("第二个共鸣2件套", ("无","满月","轻风","时钟","怒涛","魔术","顽石","水晶","寒冰","流星","烈日","大树","荆棘","钢铁"))

            gm_fm_jc_1 = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}
            gm_fm_jc_2 = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0}

            if gm_fm_1 == "满月" or gm_fm_1 == "轻风" or gm_fm_1 == "时钟" or gm_fm_1 == "怒涛" or gm_fm_1 == "魔术":
                gm_fm_jc_1["攻击"] = 0.05
                gm_fm_jc_1["智力"] = 0.05
            elif gm_fm_1 == "顽石" or gm_fm_1 == "水晶" or gm_fm_1 == "寒冰":
                gm_fm_jc_1["防御"] = 0.05
                gm_fm_jc_1["魔防"] = 0.05
            elif gm_fm_1 == "大树" or gm_fm_1 == "荆棘" or gm_fm_1 == "钢铁":
                gm_fm_jc_1["生命"] = 0.1

            if gm_fm_2 == "满月" or gm_fm_2 == "轻风" or gm_fm_2 == "时钟" or gm_fm_2 == "怒涛" or gm_fm_2 == "魔术":
                gm_fm_jc_2["攻击"] = 0.05
                gm_fm_jc_2["智力"] = 0.05
            elif gm_fm_2 == "顽石" or gm_fm_2 == "水晶" or gm_fm_2 == "寒冰":
                gm_fm_jc_2["防御"] = 0.05
                gm_fm_jc_2["魔防"] = 0.05
            elif gm_fm_2 == "大树" or gm_fm_2 == "荆棘" or gm_fm_2 == "钢铁":
                gm_fm_jc_2["生命"] = 0.1

            st.session_state.gmfm_bfb["生命"] = gm_fm_jc_1["生命"] + gm_fm_jc_2["生命"]
            st.session_state.gmfm_bfb["攻击"] = gm_fm_jc_1["攻击"] + gm_fm_jc_2["攻击"]
            st.session_state.gmfm_bfb["智力"] = gm_fm_jc_1["智力"] + gm_fm_jc_2["智力"]
            st.session_state.gmfm_bfb["防御"] = gm_fm_jc_1["防御"] + gm_fm_jc_2["防御"]
            st.session_state.gmfm_bfb["魔防"] = gm_fm_jc_1["魔防"] + gm_fm_jc_2["魔防"]

            if gm_fm_1 == gm_fm_2:
                st.session_state.gmfm_bfb["生命"] = st.session_state.gmfm_bfb["生命"]/2
                st.session_state.gmfm_bfb["攻击"] = st.session_state.gmfm_bfb["攻击"]/2
                st.session_state.gmfm_bfb["智力"] = st.session_state.gmfm_bfb["智力"]/2
                st.session_state.gmfm_bfb["防御"] = st.session_state.gmfm_bfb["防御"]/2
                st.session_state.gmfm_bfb["魔防"] = st.session_state.gmfm_bfb["魔防"]/2

        with column22:
            with st.expander("武器（百分比）附魔"):
                st.session_state.wqfm_bfb["生命"] = st.selectbox("生命%",wq_sm_bfb_percentages10,index=wq_sm_bfb_percentages10.index(st.session_state.wqfm_bfb["生命"]),key="wq_bfb_01") # 武器生命百分比附魔
                st.session_state.wqfm_bfb["攻击"] = st.selectbox("攻击%",wq_gj_bfb_percentages15,index=wq_gj_bfb_percentages15.index(st.session_state.wqfm_bfb["攻击"]),key="wq_bfb_02") # 武器攻击百分比附魔
                st.session_state.wqfm_bfb["智力"] = st.selectbox("智力%",wq_zl_bfb_percentages15,index=wq_zl_bfb_percentages15.index(st.session_state.wqfm_bfb["智力"]),key="wq_bfb_03") # 武器智力百分比附魔
                st.session_state.wqfm_bfb["防御"] = st.selectbox("防御%",wq_fy_bfb_percentages5,index=wq_fy_bfb_percentages5.index(st.session_state.wqfm_bfb["防御"]),key="wq_bfb_04") # 武器防御百分比附魔
                st.session_state.wqfm_bfb["魔防"] = st.selectbox("魔防%",wq_mf_bfb_percentages5,index=wq_mf_bfb_percentages5.index(st.session_state.wqfm_bfb["魔防"]),key="wq_bfb_05") # 武器魔防百分比附魔
            with st.expander("衣服（百分比）附魔"):
                st.session_state.yffm_bfb["生命"] = st.selectbox("生命%",yf_sm_bfb_percentages15,index=yf_sm_bfb_percentages15.index(st.session_state.yffm_bfb["生命"]),key="sf_bfb_01") # 衣服生命百分比附魔
                st.session_state.yffm_bfb["攻击"] = st.selectbox("攻击%",yf_gj_bfb_percentages5,index=yf_gj_bfb_percentages5.index(st.session_state.yffm_bfb["攻击"]),key="sf_bfb_02") # 衣服攻击百分比附魔
                st.session_state.yffm_bfb["智力"] = st.selectbox("智力%",yf_zl_bfb_percentages5,index=yf_zl_bfb_percentages5.index(st.session_state.yffm_bfb["智力"]),key="sf_bfb_03") # 衣服智力百分比附魔
                st.session_state.yffm_bfb["防御"] = st.selectbox("防御%",yf_fy_bfb_percentages15,index=yf_fy_bfb_percentages15.index(st.session_state.yffm_bfb["防御"]),key="sf_bfb_04") # 衣服防御百分比附魔
                st.session_state.yffm_bfb["魔防"] = st.selectbox("魔防%",yf_mf_bfb_percentages15,index=yf_mf_bfb_percentages15.index(st.session_state.yffm_bfb["魔防"]),key="sf_bfb_05") # 衣服魔防百分比附魔
            with st.expander("头饰（百分比）附魔"):
                st.session_state.tsfm_bfb["生命"] = st.selectbox("生命%",ts_sm_bfb_percentages15,index=ts_sm_bfb_percentages15.index(st.session_state.tsfm_bfb["生命"]),key="ts_bfb_01") # 头饰生命百分比附魔
                st.session_state.tsfm_bfb["攻击"] = st.selectbox("攻击%",ts_gj_bfb_percentages5,index=ts_gj_bfb_percentages5.index(st.session_state.tsfm_bfb["攻击"]),key="ts_bfb_02") # 头饰攻击百分比附魔
                st.session_state.tsfm_bfb["智力"] = st.selectbox("智力%",ts_zl_bfb_percentages5,index=ts_zl_bfb_percentages5.index(st.session_state.tsfm_bfb["智力"]),key="ts_bfb_03") # 头饰智力百分比附魔
                st.session_state.tsfm_bfb["防御"] = st.selectbox("防御%",ts_fy_bfb_percentages15,index=ts_fy_bfb_percentages15.index(st.session_state.tsfm_bfb["防御"]),key="ts_bfb_04") # 头饰防御百分比附魔
                st.session_state.tsfm_bfb["魔防"] = st.selectbox("魔防%",ts_mf_bfb_percentages15,index=ts_mf_bfb_percentages15.index(st.session_state.tsfm_bfb["魔防"]),key="ts_bfb_05") # 头饰魔防百分比附魔
            with st.expander("饰品（百分比）附魔"):
                st.session_state.spfm_bfb["生命"] = st.selectbox("生命%",sp_sm_bfb_percentages10,index=sp_sm_bfb_percentages10.index(st.session_state.spfm_bfb["生命"]),key="sp_bfb_01") # 饰品生命百分比附魔
                st.session_state.spfm_bfb["攻击"] = st.selectbox("攻击%",sp_gj_bfb_percentages10,index=sp_gj_bfb_percentages10.index(st.session_state.spfm_bfb["攻击"]),key="sp_bfb_02") # 饰品攻击百分比附魔
                st.session_state.spfm_bfb["智力"] = st.selectbox("智力%",sp_zl_bfb_percentages10,index=sp_zl_bfb_percentages10.index(st.session_state.spfm_bfb["智力"]),key="sp_bfb_03") # 饰品智力百分比附魔
                st.session_state.spfm_bfb["防御"] = st.selectbox("防御%",sp_fy_bfb_percentages10,index=sp_fy_bfb_percentages10.index(st.session_state.spfm_bfb["防御"]),key="sp_bfb_04") # 饰品防御百分比附魔
                st.session_state.spfm_bfb["魔防"] = st.selectbox("魔防%",sp_mf_bfb_percentages10,index=sp_mf_bfb_percentages10.index(st.session_state.spfm_bfb["魔防"]),key="sp_bfb_05") # 饰品魔防百分比附魔
        with column23:
            with st.expander("武器（固定值）附魔"):
                st.session_state.wqfm_gdz["生命"] = st.selectbox("生命固定值",wq_sm_gdz_numbers130,index=wq_sm_gdz_numbers130.index(st.session_state.wqfm_gdz["生命"]),key="wq_gdz_01") # 武器生命固定值附魔
                st.session_state.wqfm_gdz["攻击"] = st.selectbox("攻击固定值",wq_gj_gdz_numbers30,index=wq_gj_gdz_numbers30.index(st.session_state.wqfm_gdz["攻击"]),key="wq_gdz_02") # 武器攻击固定值附魔
                st.session_state.wqfm_gdz["智力"] = st.selectbox("智力固定值",wq_zl_gdz_numbers30,index=wq_zl_gdz_numbers30.index(st.session_state.wqfm_gdz["智力"]),key="wq_gdz_03") # 武器智力固定值附魔
                st.session_state.wqfm_gdz["防御"] = st.selectbox("防御固定值",wq_fy_gdz_numbers6,index=wq_fy_gdz_numbers6.index(st.session_state.wqfm_gdz["防御"]),key="wq_gdz_04") # 武器防御固定值附魔
                st.session_state.wqfm_gdz["魔防"] = st.selectbox("魔防固定值",wq_mf_gdz_numbers6,index=wq_mf_gdz_numbers6.index(st.session_state.wqfm_gdz["魔防"]),key="wq_gdz_05") # 武器魔防固定值附魔
            with st.expander("衣服（固定值）附魔"):
                st.session_state.yffm_gdz["生命"] = st.selectbox("生命固定值",yf_sm_gdz_numbers200,index=yf_sm_gdz_numbers200.index(st.session_state.yffm_gdz["生命"]),key="yf_gdz_01") # 衣服生命固定值附魔
                st.session_state.yffm_gdz["攻击"] = st.selectbox("攻击固定值",yf_gj_gdz_numbers10,index=yf_gj_gdz_numbers10.index(st.session_state.yffm_gdz["攻击"]),key="yf_gdz_02") # 衣服攻击固定值附魔
                st.session_state.yffm_gdz["智力"] = st.selectbox("智力固定值",yf_zl_gdz_numbers10,index=yf_zl_gdz_numbers10.index(st.session_state.yffm_gdz["智力"]),key="yf_gdz_03") # 衣服智力固定值附魔
                st.session_state.yffm_gdz["防御"] = st.selectbox("防御固定值",yf_fy_gdz_numbers18,index=yf_fy_gdz_numbers18.index(st.session_state.yffm_gdz["防御"]),key="yf_gdz_04") # 衣服防御固定值附魔
                st.session_state.yffm_gdz["魔防"] = st.selectbox("魔防固定值",yf_mf_gdz_numbers18,index=yf_mf_gdz_numbers18.index(st.session_state.yffm_gdz["魔防"]),key="yf_gdz_05") # 衣服魔防固定值附魔
            with st.expander("头饰（固定值）附魔"):
                st.session_state.tsfm_gdz["生命"] = st.selectbox("生命固定值",ts_sm_gdz_numbers200,index=ts_sm_gdz_numbers200.index(st.session_state.tsfm_gdz["生命"]),key="ts_gdz_01") # 头饰生命固定值附魔
                st.session_state.tsfm_gdz["攻击"] = st.selectbox("攻击固定值",ts_gj_gdz_numbers10,index=ts_gj_gdz_numbers10.index(st.session_state.tsfm_gdz["攻击"]),key="ts_gdz_02") # 头饰攻击固定值附魔
                st.session_state.tsfm_gdz["智力"] = st.selectbox("智力固定值",ts_zl_gdz_numbers10,index=ts_zl_gdz_numbers10.index(st.session_state.tsfm_gdz["智力"]),key="ts_gdz_03") # 头饰智力固定值附魔
                st.session_state.tsfm_gdz["防御"] = st.selectbox("防御固定值",ts_fy_gdz_numbers18,index=ts_fy_gdz_numbers18.index(st.session_state.tsfm_gdz["防御"]),key="ts_gdz_04") # 头饰防御固定值附魔
                st.session_state.tsfm_gdz["魔防"] = st.selectbox("魔防固定值",ts_mf_gdz_numbers18,index=ts_mf_gdz_numbers18.index(st.session_state.tsfm_gdz["魔防"]),key="ts_gdz_05") # 头饰魔防固定值附魔
            with st.expander("饰品（固定值）附魔"):
                st.session_state.spfm_gdz["生命"] = st.selectbox("生命固定值",sp_sm_gdz_numbers130,index=sp_sm_gdz_numbers130.index(st.session_state.spfm_gdz["生命"]),key="sp_gdz_01") # 饰品生命固定值附魔
                st.session_state.spfm_gdz["攻击"] = st.selectbox("攻击固定值",sp_gj_gdz_numbers20,index=sp_gj_gdz_numbers20.index(st.session_state.spfm_gdz["攻击"]),key="sp_gdz_02") # 饰品攻击固定值附魔
                st.session_state.spfm_gdz["智力"] = st.selectbox("智力固定值",sp_zl_gdz_numbers20,index=sp_zl_gdz_numbers20.index(st.session_state.spfm_gdz["智力"]),key="sp_gdz_03") # 饰品智力固定值附魔
                st.session_state.spfm_gdz["防御"] = st.selectbox("防御固定值",sp_fy_gdz_numbers12,index=sp_fy_gdz_numbers12.index(st.session_state.spfm_gdz["防御"]),key="sp_gdz_04") # 饰品防御固定值附魔
                st.session_state.spfm_gdz["魔防"] = st.selectbox("魔防固定值",sp_mf_gdz_numbers12,index=sp_mf_gdz_numbers12.index(st.session_state.spfm_gdz["魔防"]),key="sp_gdz_05") # 饰品魔防固定值附魔

        #计算总附魔加成
        #百分比总附魔加成
        st.session_state.fm_bfb["生命"] = convert_percentage_to_float(st.session_state.wqfm_bfb["生命"]) + convert_percentage_to_float(st.session_state.yffm_bfb["生命"]) + convert_percentage_to_float(st.session_state.tsfm_bfb["生命"]) + convert_percentage_to_float(st.session_state.spfm_bfb["生命"]) + st.session_state.gmfm_bfb["生命"]
        st.session_state.fm_bfb["攻击"] = convert_percentage_to_float(st.session_state.wqfm_bfb["攻击"]) + convert_percentage_to_float(st.session_state.yffm_bfb["攻击"]) + convert_percentage_to_float(st.session_state.tsfm_bfb["攻击"]) + convert_percentage_to_float(st.session_state.spfm_bfb["攻击"]) + st.session_state.gmfm_bfb["攻击"]
        st.session_state.fm_bfb["智力"] = convert_percentage_to_float(st.session_state.wqfm_bfb["智力"]) + convert_percentage_to_float(st.session_state.yffm_bfb["智力"]) + convert_percentage_to_float(st.session_state.tsfm_bfb["智力"]) + convert_percentage_to_float(st.session_state.spfm_bfb["智力"]) + st.session_state.gmfm_bfb["智力"]
        st.session_state.fm_bfb["防御"] = convert_percentage_to_float(st.session_state.wqfm_bfb["防御"]) + convert_percentage_to_float(st.session_state.yffm_bfb["防御"]) + convert_percentage_to_float(st.session_state.tsfm_bfb["防御"]) + convert_percentage_to_float(st.session_state.spfm_bfb["防御"]) + st.session_state.gmfm_bfb["防御"]
        st.session_state.fm_bfb["魔防"] = convert_percentage_to_float(st.session_state.wqfm_bfb["魔防"]) + convert_percentage_to_float(st.session_state.yffm_bfb["魔防"]) + convert_percentage_to_float(st.session_state.tsfm_bfb["魔防"]) + convert_percentage_to_float(st.session_state.spfm_bfb["魔防"]) + st.session_state.gmfm_bfb["魔防"]
        # 固定值总附魔加成
        st.session_state.fm_gdz["生命"] = st.session_state.wqfm_gdz["生命"] + st.session_state.yffm_gdz["生命"] + st.session_state.tsfm_gdz["生命"] + st.session_state.spfm_gdz["生命"]
        st.session_state.fm_gdz["攻击"] = st.session_state.wqfm_gdz["攻击"] + st.session_state.yffm_gdz["攻击"] + st.session_state.tsfm_gdz["攻击"] + st.session_state.spfm_gdz["攻击"]
        st.session_state.fm_gdz["智力"] = st.session_state.wqfm_gdz["智力"] + st.session_state.yffm_gdz["智力"] + st.session_state.tsfm_gdz["智力"] + st.session_state.spfm_gdz["智力"]
        st.session_state.fm_gdz["防御"] = st.session_state.wqfm_gdz["防御"] + st.session_state.yffm_gdz["防御"] + st.session_state.tsfm_gdz["防御"] + st.session_state.spfm_gdz["防御"]
        st.session_state.fm_gdz["魔防"] = st.session_state.wqfm_gdz["魔防"] + st.session_state.yffm_gdz["魔防"] + st.session_state.tsfm_gdz["魔防"] + st.session_state.spfm_gdz["魔防"]

        #创建附魔加成统计表格 DataFrame
        column24, column25= st.columns([1.2,1])
        with column24:
            st.markdown("""<h5 style='text-align: center;'>附魔百分比加成统计表</h5>""",unsafe_allow_html=True)
            fm_bfb_jc_data = {
                "属性": ["生命", "攻击", "智力", "防御", "魔防"],
                "武器": list(st.session_state.wqfm_bfb.values()),
                "衣服": list(st.session_state.yffm_bfb.values()),
                "头饰": list(st.session_state.tsfm_bfb.values()),
                "饰品": list(st.session_state.spfm_bfb.values()),
                "共鸣": [f"{round(value * 100)}%" for value in st.session_state.gmfm_bfb.values()],
                "合计": [f"{round(value * 100)}%" for value in st.session_state.fm_bfb.values()]
            }
            st.dataframe(fm_bfb_jc_data)
        with column25:
            st.markdown("""<h5 style='text-align: center;'>附魔固定值加成统计表</h5>""",unsafe_allow_html=True)
            fm_gdz_jc_data = {
                "属性": ["生命", "攻击", "智力", "防御", "魔防"],
                "武器": list(st.session_state.wqfm_gdz.values()),
                "衣服": list(st.session_state.yffm_gdz.values()),
                "头饰": list(st.session_state.tsfm_gdz.values()),
                "饰品": list(st.session_state.spfm_gdz.values()),
                "合计": list(st.session_state.fm_gdz.values())
            }
            st.dataframe(fm_gdz_jc_data)

    with tab3:
        column31,column32,column33 = st.columns([0.4,1,0.3])
        with column31:
            zyjt_jfm = st.radio("职业精通是否满值", ("默认满", "自定义"))
        with column32:
            if zyjt_jfm == "默认满":
                st.session_state.zyjt["生命"] = 750
                st.session_state.zyjt["攻击"] = 80
                st.session_state.zyjt["智力"] = 80
                st.session_state.zyjt["防御"] = 60
                st.session_state.zyjt["魔防"] = 60
                st.session_state.zyjt["技巧"] = 80
                st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zyjt["生命"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zyjt["攻击"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zyjt["智力"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zyjt["防御"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zyjt["魔防"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zyjt["技巧"]}</span></strong>",unsafe_allow_html=True)
            else:
                st.session_state.zyjt["生命"] = st.number_input("生命-职业精通", value=st.session_state.zyjt["生命"])  # 生命职业精通
                st.session_state.zyjt["攻击"] = st.number_input("攻击-职业精通", value=st.session_state.zyjt["攻击"])  # 攻击职业精通
                st.session_state.zyjt["智力"] = st.number_input("智力-职业精通", value=st.session_state.zyjt["智力"])  # 智力职业精通
                st.session_state.zyjt["防御"] = st.number_input("防御-职业精通", value=st.session_state.zyjt["防御"])  # 防御职业精通
                st.session_state.zyjt["魔防"] = st.number_input("魔防-职业精通", value=st.session_state.zyjt["魔防"])  # 魔防职业精通
                st.session_state.zyjt["技巧"] = st.number_input("技巧-职业精通", value=st.session_state.zyjt["技巧"])  # 技巧职业精通

    with tab4:
        column41, column42, column43 = st.columns([0.8, 1, 0.3])
        with column41:
            zw_xz = st.radio("选择铸纹类型（默认满级）", ("无", "攻击英雄", "智力英雄", "双修英雄(火男、黑骑士)", "双修英雄(阿卡娅)","自定义铸纹"))
        with column42:
            if zw_xz == "无":
                st.session_state.zw["生命"] = 0
                st.session_state.zw["攻击"] = 0
                st.session_state.zw["智力"] = 0
                st.session_state.zw["防御"] = 0
                st.session_state.zw["魔防"] = 0
                st.session_state.zw["技巧"] = 0
            elif zw_xz == "攻击英雄":
                st.session_state.zw["生命"] = 1000
                st.session_state.zw["攻击"] = 150
                st.session_state.zw["智力"] = 30
                st.session_state.zw["防御"] = 90
                st.session_state.zw["魔防"] = 90
                st.session_state.zw["技巧"] = 20
            elif zw_xz == "智力英雄":
                st.session_state.zw["生命"] = 1000
                st.session_state.zw["攻击"] = 30
                st.session_state.zw["智力"] = 150
                st.session_state.zw["防御"] = 90
                st.session_state.zw["魔防"] = 90
                st.session_state.zw["技巧"] = 20
            elif zw_xz == "双修英雄(火男、黑骑士)":
                st.session_state.zw["生命"] = 800
                st.session_state.zw["攻击"] = 150
                st.session_state.zw["智力"] = 110
                st.session_state.zw["防御"] = 90
                st.session_state.zw["魔防"] = 90
                st.session_state.zw["技巧"] = 20
            elif zw_xz == "双修英雄(阿卡娅)":
                st.session_state.zw["生命"] = 800
                st.session_state.zw["攻击"] = 110
                st.session_state.zw["智力"] = 150
                st.session_state.zw["防御"] = 90
                st.session_state.zw["魔防"] = 90
                st.session_state.zw["技巧"] = 20
            elif zw_xz == "自定义铸纹":
                st.session_state.zw["生命"] = st.number_input("生命-铸纹加成", value=st.session_state.zw["生命"])  # 生命铸纹绿字
                st.session_state.zw["攻击"] = st.number_input("攻击-铸纹加成", value=st.session_state.zw["攻击"])  # 攻击铸纹绿字
                st.session_state.zw["智力"] = st.number_input("智力-铸纹加成", value=st.session_state.zw["智力"])  # 智力铸纹绿字
                st.session_state.zw["防御"] = st.number_input("防御-铸纹加成", value=st.session_state.zw["防御"])  # 防御铸纹绿字
                st.session_state.zw["魔防"] = st.number_input("魔防-铸纹加成", value=st.session_state.zw["魔防"])  # 魔防铸纹绿字
                st.session_state.zw["技巧"] = st.number_input("技巧-铸纹加成", value=st.session_state.zw["技巧"])  # 技巧铸纹绿字

            if zw_xz != "自定义铸纹":
                st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zw["生命"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zw["攻击"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zw["智力"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zw["防御"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zw["魔防"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> + {st.session_state.zw["技巧"]}</span></strong>",unsafe_allow_html=True)

    with tab5:
        # 神契神力石板加成 字典
        sq_slsb_dict = {
            "未携带": {"生命": 0, "攻击": 0, "智力": 0, "防御": 0, "魔防": 0, "技巧": 0, "士兵生命": 0, "士兵攻击": 0, "士兵防御": 0, "士兵魔防": 0},
            "索尔": {"生命": 360, "攻击": 45, "智力": 45, "防御": 30, "魔防": 30, "技巧": 10, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
            "菲依雅": {"生命": 180, "攻击": 18, "智力": 75, "防御": 28, "魔防": 50, "技巧": 9, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
            "海姆达尔": {"生命": 500, "攻击": 24, "智力": 18, "防御": 82, "魔防": 6, "技巧": 5, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
            "巴德尔": {"生命": 380, "攻击": 21, "智力": 72, "防御": 46, "魔防": 12, "技巧": 9, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
            "奥丁": {"生命": 300, "攻击": 93, "智力": 12, "防御": 36, "魔防": 10, "技巧": 15, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
            "弗丽嘉": {"生命": 420, "攻击": 18, "智力": 27, "防御": 8, "魔防": 86, "技巧": 5, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
            "提尔": {"生命": 460, "攻击": 96, "智力": 18, "防御": 28, "魔防": 10, "技巧": 8, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
            "洛基": {"生命": 400, "攻击": 12, "智力": 120, "防御": 10, "魔防": 18, "技巧": 10, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06},
            "维达": {"生命": 400, "攻击": 69, "智力": 21, "防御": 14, "魔防": 44, "技巧": 9, "士兵生命": 0.06, "士兵攻击": 0.06, "士兵防御": 0.06, "士兵魔防": 0.06}
        }
        # 用户选择框
        st.session_state.selected_sq = st.selectbox("请选择神契", list(sq_slsb_dict.keys()))
        # 更新 神契神力石板加成
        if st.session_state.selected_sq and st.session_state.selected_sq in sq_slsb_dict:
            st.session_state.sq_slsb = sq_slsb_dict[st.session_state.selected_sq]

        with st.expander("（点击打开输入自己的）神契晨曦之祝加成"):
            column51,column52 = st.columns([0.5,1])
            with column51:
                st.write("### 神力石板加成")
                st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_slsb["生命"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_slsb["攻击"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_slsb["智力"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_slsb["防御"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_slsb["魔防"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_slsb["技巧"]}</span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 士兵生命: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_slsb["士兵生命"]*100}% </span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 士兵攻击: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_slsb["士兵攻击"]*100}% </span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 士兵防御: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_slsb["士兵防御"]*100}% </span></strong>",unsafe_allow_html=True)
                st.markdown(f"#### 士兵魔防: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_slsb["士兵魔防"]*100}% </span></strong>",unsafe_allow_html=True)

            with column52:
                st.write("### 晨曦之祝加成")
                # 神契晨曦之祝加成
                column521, column522 = st.columns([1, 1])
                with column521:
                    st.session_state.sq_cxzz["生命"] = st.number_input("生命（最大值600）", value=st.session_state.sq_cxzz["生命"])  # 生命晨曦绿字
                    st.session_state.sq_cxzz["攻击"] = st.number_input("攻击（最大值75）", value=st.session_state.sq_cxzz["攻击"])  # 攻击晨曦绿字
                    st.session_state.sq_cxzz["智力"] = st.number_input("智力（最大值75）", value=st.session_state.sq_cxzz["智力"])  # 智力晨曦绿字
                with column522:
                    st.session_state.sq_cxzz["防御"] = st.number_input("防御（最大值60）", value=st.session_state.sq_cxzz["防御"])  # 防御晨曦绿字
                    st.session_state.sq_cxzz["魔防"] = st.number_input("魔防（最大值60）", value=st.session_state.sq_cxzz["魔防"])  # 魔防晨曦绿字
                    st.session_state.sq_cxzz["技巧"] = st.number_input("技巧（最大值0）", value=st.session_state.sq_cxzz["技巧"])  # 技巧晨曦绿字
                st.session_state.sq_cxzz_sbgd["士兵生命"] = st.text_input("士兵生命%（最大值18%）", value=st.session_state.sq_cxzz_sbgd["士兵生命"])  # 士兵生命晨曦加成百分比
                st.session_state.sq_cxzz_sbgd["士兵攻击"] = st.text_input("士兵攻击%（最大值18%）", value=st.session_state.sq_cxzz_sbgd["士兵攻击"])  # 士兵攻击晨曦加成百分比
                st.session_state.sq_cxzz_sbgd["士兵防御"] = st.text_input("士兵防御%（最大值18%）", value=st.session_state.sq_cxzz_sbgd["士兵防御"])  # 士兵防御晨曦加成百分比
                st.session_state.sq_cxzz_sbgd["士兵魔防"] = st.text_input("士兵魔防%（最大值18%）", value=st.session_state.sq_cxzz_sbgd["士兵魔防"])  # 士兵魔防晨曦加成百分比
                st.session_state.sq_cxzz["士兵生命"] = bfb_shuru(st.session_state.sq_cxzz_sbgd["士兵生命"])
                st.session_state.sq_cxzz["士兵攻击"] = bfb_shuru(st.session_state.sq_cxzz_sbgd["士兵攻击"])
                st.session_state.sq_cxzz["士兵防御"] = bfb_shuru(st.session_state.sq_cxzz_sbgd["士兵防御"])
                st.session_state.sq_cxzz["士兵魔防"] = bfb_shuru(st.session_state.sq_cxzz_sbgd["士兵魔防"])

        st.write("### 神契总加成")
        # 神契总加成
        st.session_state.sq_zjc["生命"] = st.session_state.sq_slsb["生命"] + st.session_state.sq_cxzz["生命"]
        st.session_state.sq_zjc["攻击"] = st.session_state.sq_slsb["攻击"] + st.session_state.sq_cxzz["攻击"]
        st.session_state.sq_zjc["智力"] = st.session_state.sq_slsb["智力"] + st.session_state.sq_cxzz["智力"]
        st.session_state.sq_zjc["防御"] = st.session_state.sq_slsb["防御"] + st.session_state.sq_cxzz["防御"]
        st.session_state.sq_zjc["魔防"] = st.session_state.sq_slsb["魔防"] + st.session_state.sq_cxzz["魔防"]
        st.session_state.sq_zjc["技巧"] = st.session_state.sq_slsb["技巧"] + st.session_state.sq_cxzz["技巧"]
        st.session_state.sq_zjc["士兵生命"] = st.session_state.sq_slsb["士兵生命"] + st.session_state.sq_cxzz["士兵生命"]
        st.session_state.sq_zjc["士兵攻击"] = st.session_state.sq_slsb["士兵攻击"] + st.session_state.sq_cxzz["士兵攻击"]
        st.session_state.sq_zjc["士兵防御"] = st.session_state.sq_slsb["士兵防御"] + st.session_state.sq_cxzz["士兵防御"]
        st.session_state.sq_zjc["士兵魔防"] = st.session_state.sq_slsb["士兵魔防"] + st.session_state.sq_cxzz["士兵魔防"]

        column53, column54 = st.columns([1, 1])
        with column53:
            st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_zjc["生命"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_zjc["攻击"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_zjc["智力"]}</span></strong>",unsafe_allow_html=True)
        with column54:
            st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_zjc["防御"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_zjc["魔防"]}</span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_zjc["技巧"]}</span></strong>",unsafe_allow_html=True)
        column55, column56 = st.columns([1, 1])
        with column55:
            st.markdown(f"#### 士兵生命: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_zjc["士兵生命"]*100}% </span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 士兵攻击: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_zjc["士兵攻击"]*100}% </span></strong>",unsafe_allow_html=True)
        with column56:
            st.markdown(f"#### 士兵防御: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_zjc["士兵防御"]*100}% </span></strong>",unsafe_allow_html=True)
            st.markdown(f"#### 士兵魔防: <strong><span style='color:green;font-size:25px;'> + {st.session_state.sq_zjc["士兵魔防"]*100}% </span></strong>",unsafe_allow_html=True)

    with tab6:
        st.session_state.lz["生命"] = st.session_state.zb_jc["生命"] + st.session_state.bz["生命"]*st.session_state.fm_bfb["生命"] + st.session_state.fm_gdz["生命"] + st.session_state.zyjt["生命"] + st.session_state.zw["生命"] + st.session_state.sq_zjc["生命"]
        st.session_state.lz["攻击"] = st.session_state.zb_jc["攻击"] + st.session_state.bz["攻击"]*st.session_state.fm_bfb["攻击"] + st.session_state.fm_gdz["攻击"] + st.session_state.zyjt["攻击"] + st.session_state.zw["攻击"] + st.session_state.sq_zjc["攻击"]
        st.session_state.lz["智力"] = st.session_state.zb_jc["智力"] + st.session_state.bz["智力"]*st.session_state.fm_bfb["智力"] + st.session_state.fm_gdz["智力"] + st.session_state.zyjt["智力"] + st.session_state.zw["智力"] + st.session_state.sq_zjc["智力"]
        st.session_state.lz["防御"] = st.session_state.zb_jc["防御"] + st.session_state.bz["防御"]*st.session_state.fm_bfb["防御"] + st.session_state.fm_gdz["防御"] + st.session_state.zyjt["防御"] + st.session_state.zw["防御"] + st.session_state.sq_zjc["防御"]
        st.session_state.lz["魔防"] = st.session_state.zb_jc["魔防"] + st.session_state.bz["魔防"]*st.session_state.fm_bfb["魔防"] + st.session_state.fm_gdz["魔防"] + st.session_state.zyjt["魔防"] + st.session_state.zw["魔防"] + st.session_state.sq_zjc["魔防"]
        st.session_state.lz["技巧"] = st.session_state.zb_jc["技巧"] + st.session_state.zyjt["技巧"] + st.session_state.zw["技巧"] + st.session_state.sq_zjc["技巧"]

        st.markdown(f"#### 生命: <strong><span style='color:green;font-size:25px;'> + {st.session_state.lz["生命"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 攻击: <strong><span style='color:green;font-size:25px;'> + {st.session_state.lz["攻击"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 智力: <strong><span style='color:green;font-size:25px;'> + {st.session_state.lz["智力"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 防御: <strong><span style='color:green;font-size:25px;'> + {st.session_state.lz["防御"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 魔防: <strong><span style='color:green;font-size:25px;'> + {st.session_state.lz["魔防"]}</span></strong>",unsafe_allow_html=True)
        st.markdown(f"#### 技巧: <strong><span style='color:green;font-size:25px;'> + {st.session_state.lz["技巧"]}</span></strong>",unsafe_allow_html=True)

    # 分割线
    st.divider()

    st.markdown("""<h5 style='text-align: center;'>英雄绿字加成统计表</h5>""", unsafe_allow_html=True)

    # 创建数据表 英雄绿字加成统计表
    lz_jc_data = {
        "合计": list(st.session_state.lz.values()),
        "装备基础": list(st.session_state.zb_jc.values()),
        "附魔百分比": [f"{round(value*100)}%" for value in st.session_state.fm_bfb.values()]+["-"] ,
        "附魔百分比*白字": [
            st.session_state.bz["生命"]*st.session_state.fm_bfb["生命"],
            st.session_state.bz["攻击"]*st.session_state.fm_bfb["攻击"],
            st.session_state.bz["智力"]*st.session_state.fm_bfb["智力"],
            st.session_state.bz["防御"]*st.session_state.fm_bfb["防御"],
            st.session_state.bz["魔防"]*st.session_state.fm_bfb["魔防"],
            "-",
        ],
        "附魔固定值": list(st.session_state.fm_gdz.values())+["-"],
        "职业精通": list(st.session_state.zyjt.values()),
        "铸纹": list(st.session_state.zw.values()),
        "神契": [
            st.session_state.sq_zjc["生命"],
            st.session_state.sq_zjc["攻击"],
            st.session_state.sq_zjc["智力"],
            st.session_state.sq_zjc["防御"],
            st.session_state.sq_zjc["魔防"],
            st.session_state.sq_zjc["技巧"],
        ],
    }

    # 将属性作为行索引
    df1 = pd.DataFrame(lz_jc_data, index=["生命", "攻击", "智力", "防御", "魔防", "技巧"])

    # 显示为DataFrame
    st.dataframe(df1,use_container_width=True)

    # 分割线
    st.divider()

    st.write("### 英雄竞技精通区")
    st.session_state.jjjt["生命"] = st.number_input("生命-竞技精通", value=st.session_state.jjjt["生命"])  # 生命竞技精通
    st.session_state.jjjt["攻击"] = st.number_input("攻击-竞技精通", value=st.session_state.jjjt["攻击"])  # 攻击竞技精通
    st.session_state.jjjt["智力"] = st.number_input("智力-竞技精通", value=st.session_state.jjjt["智力"])  # 智力竞技精通
    st.session_state.jjjt["防御"] = st.number_input("防御-竞技精通", value=st.session_state.jjjt["防御"])  # 防御竞技精通
    st.session_state.jjjt["魔防"] = st.number_input("魔防-竞技精通", value=st.session_state.jjjt["魔防"])  # 魔防竞技精通
    st.session_state.jjjt["技巧"] = st.number_input("技巧-竞技精通", value=st.session_state.jjjt["技巧"])  # 技巧竞技精通

elif selection == "士兵面板模拟":
    st.write("### 英雄兵修区（未开发）")
    sm_bx = st.number_input("生命-兵修", 0)  # 生命兵修
    gj_bx = st.number_input("攻击-兵修", 0)  # 攻击兵修
    fy_bx = st.number_input("防御-兵修", 0)  # 防御兵修
    mf_bx = st.number_input("魔防-兵修", 0)  # 魔防兵修

elif selection == "神契设置":
    st.write("### 神契区（未开发）")

    # 选择神契
    sf_dx = st.selectbox("神契",("无神契", "索尔", "菲依雅", "海姆达尔", "巴德尔", "奥丁", "弗丽嘉", "提尔", "洛基", "维达"))

    st.write("### 全部加成")

    st.write("### 神力石板加成（默认满）")

    st.write("##### 英雄加成（默认满）")

    st.write("##### 士兵加成（默认满）")

    st.write("### 晨曦之祝加成（根据自己情况调整）")
    st.write("##### 英雄加成")

    st.write("##### 士兵加成")


    st.image("./image/头像_辉耀圣召使.png") #测试图片载入


