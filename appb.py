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
    st.session_state.jjjt = {"生命":0,"攻击":0,"智力":0,"防御":0,"魔防":0,"技巧":0}  # 初始化职业精通 字典

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

    st.write("### 英雄白字区")
    st.session_state.bz["生命"] = st.number_input("生命-白字", value=st.session_state.bz["生命"])  # 生命白字
    st.session_state.bz["攻击"] = st.number_input("攻击-白字", value=st.session_state.bz["攻击"])  # 攻击白字
    st.session_state.bz["智力"] = st.number_input("智力-白字", value=st.session_state.bz["智力"])  # 智力白字
    st.session_state.bz["防御"] = st.number_input("防御-白字", value=st.session_state.bz["防御"])  # 防御白字
    st.session_state.bz["魔防"] = st.number_input("魔防-白字", value=st.session_state.bz["魔防"])  # 魔防白字
    st.session_state.bz["技巧"] = st.number_input("技巧-白字", value=st.session_state.bz["技巧"])  # 技巧白字

    st.write("### 英雄绿字区")

    st.write("### 铸纹区")
    st.session_state.zw["生命"] = st.number_input("生命-铸纹加成", value=st.session_state.zw["生命"])  # 生命铸纹绿字
    st.session_state.zw["攻击"] = st.number_input("攻击-铸纹加成", value=st.session_state.zw["攻击"])  # 攻击铸纹绿字
    st.session_state.zw["智力"] = st.number_input("智力-铸纹加成", value=st.session_state.zw["智力"])  # 智力铸纹绿字
    st.session_state.zw["防御"] = st.number_input("防御-铸纹加成", value=st.session_state.zw["防御"])  # 防御铸纹绿字
    st.session_state.zw["魔防"] = st.number_input("魔防-铸纹加成", value=st.session_state.zw["魔防"])  # 魔防铸纹绿字
    st.session_state.zw["技巧"] = st.number_input("技巧-铸纹加成", value=st.session_state.zw["技巧"])  # 技巧铸纹绿字

    st.write("### 职业精通区")
    st.session_state.zyjt["生命"] = st.number_input("生命-职业精通", value=st.session_state.zyjt["生命"])  # 生命职业精通
    st.session_state.zyjt["攻击"] = st.number_input("攻击-职业精通", value=st.session_state.zyjt["攻击"])  # 攻击职业精通
    st.session_state.zyjt["智力"] = st.number_input("智力-职业精通", value=st.session_state.zyjt["智力"])  # 智力职业精通
    st.session_state.zyjt["防御"] = st.number_input("防御-职业精通", value=st.session_state.zyjt["防御"])  # 防御职业精通
    st.session_state.zyjt["魔防"] = st.number_input("魔防-职业精通", value=st.session_state.zyjt["魔防"])  # 魔防职业精通
    st.session_state.zyjt["技巧"] = st.number_input("技巧-职业精通", value=st.session_state.zyjt["技巧"])  # 技巧职业精通

    st.write("### 英雄竞技精通区")
    st.session_state.jjjt["生命"] = st.number_input("生命-竞技精通", value=st.session_state.jjjt["生命"])  # 生命竞技精通
    st.session_state.jjjt["攻击"] = st.number_input("攻击-竞技精通", value=st.session_state.jjjt["攻击"])  # 攻击竞技精通
    st.session_state.jjjt["智力"] = st.number_input("智力-竞技精通", value=st.session_state.jjjt["智力"])  # 智力竞技精通
    st.session_state.jjjt["防御"] = st.number_input("防御-竞技精通", value=st.session_state.jjjt["防御"])  # 防御竞技精通
    st.session_state.jjjt["魔防"] = st.number_input("魔防-竞技精通", value=st.session_state.jjjt["魔防"])  # 魔防竞技精通
    st.session_state.jjjt["技巧"] = st.number_input("技巧-竞技精通", value=st.session_state.jjjt["技巧"])  # 技巧竞技精通

elif selection == "士兵面板模拟":
    st.write("### 英雄兵修区")
    sm_bx = st.number_input("生命-兵修", 0)  # 生命兵修
    gj_bx = st.number_input("攻击-兵修", 0)  # 攻击兵修
    fy_bx = st.number_input("防御-兵修", 0)  # 防御兵修
    mf_bx = st.number_input("魔防-兵修", 0)  # 魔防兵修

elif selection == "神契设置":
    st.write("### 神契区")

    # 选择神契
    sf_dx = st.selectbox("神契",("无神契", "索尔", "菲依雅", "海姆达尔", "巴德尔", "奥丁", "弗丽嘉", "提尔", "洛基", "维达"))

    st.write("### 全部加成")

    st.write("### 神力石板加成（默认满）")

    st.write("##### 英雄加成（默认满）")

    st.write("##### 士兵加成（默认满）")

    st.write("### 晨曦之祝加成（根据自己情况调整）")
    st.write("##### 英雄加成")

    st.write("##### 士兵加成")

    st.image("./image/头像_辉耀圣召使.png")


