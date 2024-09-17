import math
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
st.title('梦幻模拟战-单点模拟计算器')

column1, column2, column3 = st.columns([1,0.3,1])

with column1:
    st.write("### 攻方")
    tab1, tab2 = st.tabs(["士兵", "英雄"])
    with tab1:
        # 定义攻方士兵攻击
        gf_sbgj = st.text_input("攻方士兵攻击", "0")
        gf_sbgj = mb_shuru(gf_sbgj)

        sb_bdb_kzpd = st.checkbox("兵与兵 有克制关系")
        if sb_bdb_kzpd:
            # 定义攻方士兵对士兵攻智克制系数
            gf_sbdsb_gzkzxs = st.text_input("士兵对士兵攻智克制系数加成%", "0")
            gf_sbdsb_gzkzxs = bfb_shuru(gf_sbdsb_gzkzxs)
        else:
            gf_sbdsb_gzkzxs = 0
        sb_bdyx_kzpd = st.checkbox("兵与英雄 有克制关系")
        if sb_bdyx_kzpd:
            # 定义攻方士兵对英雄攻智克制系数
            gf_sbdyx_gzkzxs = st.text_input("士兵对英雄攻智克制系数加成%", "0")
            gf_sbdyx_gzkzxs = bfb_shuru(gf_sbdyx_gzkzxs)
        else:
            gf_sbdyx_gzkzxs = 0

        column11, column12 = st.columns([1, 1])
        with column11:
            # 选择物理还是魔法伤害
            sbsh_lx = st.radio("士兵伤害类型", ("物理", "魔法"))
        with column12:
            # 定义攻方士兵无视双防系数
            gf_sb_wsfy = st.text_input("士兵无视双防系数%", "0")
            gf_sb_wsfy = bfb_shuru(gf_sb_wsfy)
            # 定义攻方士兵技能倍率
            gf_sbjnbl = st.text_input("攻方士兵技能倍率", "1")
            gf_sbjnbl = mb_shuru(gf_sbjnbl)
        # 定义攻方士兵通用增伤
        gf_sb_tyzs = st.text_input("攻方士兵通用增伤%", "0")
        gf_sb_tyzs = bfb_shuru(gf_sb_tyzs)
        column13, column14 = st.columns([1, 1])
        with column13:
            # 定义攻方士兵技能增伤
            gf_sb_jnzs = st.text_input("攻方士兵技能增伤%", "0")
            gf_sb_jnzs = bfb_shuru(gf_sb_jnzs)
            # 定义攻方士兵远程增伤
            gf_sb_yczs = st.text_input("攻方士兵远程增伤%", "0")
            gf_sb_yczs = bfb_shuru(gf_sb_yczs)
        with column14:
            # 定义攻方士兵其他增伤
            gf_sb_qtzs = st.text_input("攻方士兵其他增伤%", "0")
            gf_sb_qtzs = bfb_shuru(gf_sb_qtzs)
            # 定义攻方士兵暴伤加成
            gf_sb_bs = st.text_input("攻方士兵暴伤加成%", "0")
            gf_sb_bs = bfb_shuru(gf_sb_bs)
    with tab2:
        # 定义攻方英雄攻击
        gf_yxgj = st.text_input("攻方英雄攻击", "0")
        gf_yxgj = mb_shuru(gf_yxgj)
        # 定义攻方英雄智力
        gf_yxzl = st.text_input("攻方英雄智力", "0")
        gf_yxzl = mb_shuru(gf_yxzl)

        yx_yxdb_kzpd = st.checkbox("英雄与兵 有克制关系")
        if yx_yxdb_kzpd:
            # 定义攻方英雄对士兵攻智克制系数
            gf_yxdsb_gzkzxs = st.text_input("英雄对士兵攻智克制系数加成%", "0")
            gf_yxdsb_gzkzxs = bfb_shuru(gf_yxdsb_gzkzxs)
        else:
            gf_yxdsb_gzkzxs = 0
        yx_yxdyx_kzpd = st.checkbox("英雄与英雄 有克制关系")
        if yx_yxdyx_kzpd:
            # 定义攻方英雄对英雄攻智克制系数
            gf_yxdyx_gzkzxs = st.text_input("英雄对英雄攻智克制系数加成%", "0")
            gf_yxdyx_gzkzxs = bfb_shuru(gf_yxdyx_gzkzxs)
        else:
            gf_yxdyx_gzkzxs = 0

        column21, column22 = st.columns([1, 1])
        with column21:
            # 选择物理还是魔法伤害
            yxsh_lx = st.radio("英雄伤害类型", ("物理", "魔法"))
        with column22:
            # 定义攻方英雄无视双防系数
            gf_yx_wsfy = st.text_input("无视双防系数%", "0")
            gf_yx_wsfy = bfb_shuru(gf_yx_wsfy)
            # 定义攻方英雄技能倍率
            gf_yxjnbl = st.text_input("攻方英雄技能倍率", "1")
            gf_yxjnbl = mb_shuru(gf_yxjnbl)
        # 定义攻方英雄物理通用增伤
        gf_yx_tyzs = st.text_input("攻方英雄通用增伤%", "0")
        gf_yx_tyzs = bfb_shuru(gf_yx_tyzs)
        column23, column24 = st.columns([1, 1])
        with column23:
            # 定义攻方英雄技能增伤
            gf_yx_jnzs = st.text_input("攻方英雄技能增伤%", "0")
            gf_yx_jnzs = bfb_shuru(gf_yx_jnzs)
            # 定义攻方英雄远程增伤
            gf_yx_yczs = st.text_input("攻方英雄远程增伤%", "0")
            gf_yx_yczs = bfb_shuru(gf_yx_yczs)
        with column24:
            # 定义攻方英雄其他增伤
            gf_yx_qtzs = st.text_input("攻方英雄其他增伤%", "0")
            gf_yx_qtzs = bfb_shuru(gf_yx_qtzs)
            # 定义攻方英雄暴伤加成
            gf_yx_bs = st.text_input("攻方英雄暴伤加成%", "0")
            gf_yx_bs = bfb_shuru(gf_yx_bs)
        # 选择攻方英雄攻击段数是否为20段
        gf_yx_gjdspd = st.checkbox("攻方英雄攻击段数是否为20段", value=True)
        if gf_yx_gjdspd:
            gf_yx_gjds = 20  # 默认为20
        else:
            gf_yx_gjds = st.number_input("攻方英雄攻击段数", min_value=1, value=40)

with column3:
    st.write("### 守方")
    tab3, tab4 = st.tabs(["士兵", "英雄"])
    with tab3:
        column31, column32 = st.columns([1, 1])
        with column31:
            # 定义守方士兵防御
            sf_sbfy = st.text_input("守方士兵防御", "0")
            sf_sbfy = mb_shuru(sf_sbfy)
        with column32:
            # 定义守方士兵魔防
            sf_sbmf = st.text_input("守方士兵魔防", "0")
            sf_sbmf = mb_shuru(sf_sbmf)

        if sb_bdb_kzpd:
            # 定义守方士兵与攻方士兵交战时双防克制系数加成
            sf_sbdsb_sfkzxs = st.text_input("士兵与 攻方士兵 交战时双防克制系数加成%", "0")
            sf_sbdsb_sfkzxs = bfb_shuru(sf_sbdsb_sfkzxs)
        else:
            sf_sbdsb_sfkzxs = 0
        if yx_yxdb_kzpd:
            # 定义守方士兵与攻方英雄交战时双防克制系数加成
            sf_sbdyx_sfkzxs = st.text_input("士兵与 攻方英雄 交战时双防克制系数加成%", "0")
            sf_sbdyx_sfkzxs = bfb_shuru(sf_sbdyx_sfkzxs)
        else:
            sf_sbdyx_sfkzxs = 0

        # 定义守方士兵物理通用减伤
        sf_sb_wl_tyjs = st.text_input("守方士兵物理通用减伤%", "0")
        sf_sb_wl_tyjs = bfb_shuru(sf_sb_wl_tyjs)
        # 定义守方士兵魔法通用减伤
        sf_sb_mf_tyjs = st.text_input("守方士兵魔法通用减伤%", "0")
        sf_sb_mf_tyjs = bfb_shuru(sf_sb_mf_tyjs)
        column33, column34 = st.columns([1, 1])
        with column33:
            # 定义守方士兵技能减伤
            sf_sb_jnjs = st.text_input("守方士兵技能减伤%", "0")
            sf_sb_jnjs = bfb_shuru(sf_sb_jnjs)
            # 定义守方士兵远程减伤
            sf_sb_ycjs = st.text_input("守方士兵远程减伤%", "0")
            sf_sb_ycjs = bfb_shuru(sf_sb_ycjs)
        with column34:
            # 定义守方士兵其他减伤
            sf_sb_qtjs = st.text_input("守方士兵其他减伤%", "0")
            sf_sb_qtjs = bfb_shuru(sf_sb_qtjs)
            # 定义守方士兵减暴伤
            sf_sb_jbs = st.text_input("守方士兵减暴伤%", "0")
            sf_sb_jbs = bfb_shuru(sf_sb_jbs)
    with tab4:
        # 定义守方英雄防御
        sf_yxfy = st.text_input("守方英雄防御", "0")
        sf_yxfy = mb_shuru(sf_yxfy)
        # 定义守方英雄魔防
        sf_yxmf = st.text_input("守方英雄魔防", "0")
        sf_yxmf = mb_shuru(sf_yxmf)

        if sb_bdyx_kzpd:
            # 定义守方英雄与攻方士兵交战时双防克制系数加成
            sf_yxdsb_sfkzxs = st.text_input("英雄与 攻方士兵 交战时双防克制系数加成%", "0")
            sf_yxdsb_sfkzxs = bfb_shuru(sf_yxdsb_sfkzxs)
        else:
            sf_yxdsb_sfkzxs = 0
        if yx_yxdyx_kzpd:
            # 定义守方英雄与攻方英雄交战时双防克制系数加成
            sf_yxdyx_sfkzxs = st.text_input("英雄与 攻方英雄 交战时双防克制系数加成%", "0")
            sf_yxdyx_sfkzxs = bfb_shuru(sf_yxdyx_sfkzxs)
        else:
            sf_yxdyx_sfkzxs = 0

        # 定义守方英雄物理通用减伤
        sf_yx_wl_tyjs = st.text_input("守方英雄物理通用减伤%", "0")
        sf_yx_wl_tyjs = bfb_shuru(sf_yx_wl_tyjs)
        # 定义守方英雄魔法通用减伤
        sf_yx_mf_tyjs = st.text_input("守方英雄魔法通用减伤%", "0")
        sf_yx_mf_tyjs = bfb_shuru(sf_yx_mf_tyjs)
        column41, column42 = st.columns([1, 1])
        with column41:
            # 定义守方英雄技能减伤
            sf_yx_jnjs = st.text_input("守方英雄技能减伤%", "0")
            sf_yx_jnjs = bfb_shuru(sf_yx_jnjs)
            # 定义守方英雄远程减伤
            sf_yx_ycjs = st.text_input("守方英雄远程减伤%", "0")
            sf_yx_ycjs = bfb_shuru(sf_yx_ycjs)
        with column42:
            # 定义守方英雄其他减伤
            sf_yx_qtjs = st.text_input("守方英雄其他减伤%", "0")
            sf_yx_qtjs = bfb_shuru(sf_yx_qtjs)
            # 定义守方英雄减暴伤
            sf_yx_jbs = st.text_input("守方英雄减暴伤%", "0")
            sf_yx_jbs = bfb_shuru(sf_yx_jbs)

    # 分割线
    st.divider()

    # 定义守方地形
    sf_dx = st.selectbox("守方地形", ("无地形", "树林", "城墙", "山地", "基岩", "货物", "沙丘", "礁石", "石柱"))
    # 定义守方地形修正 sf_dxxz
    # 根据地形判断地形修正
    if sf_dx == "无地形":
        sf_dxxz = 0
    elif sf_dx == "树林":
        sf_dxxz = 0.2
    elif sf_dx == "城墙":
        sf_dxxz = 0.3
    elif sf_dx == "山地":
        sf_dxxz = 0.1
    elif sf_dx == "基岩":
        sf_dxxz = 0.2
    elif sf_dx == "货物":
        sf_dxxz = 0.15
    elif sf_dx == "沙丘":
        sf_dxxz = 0.1
    elif sf_dx == "礁石":
        sf_dxxz = 0.05
    else:
        sf_dxxz = 0.05
    # 输出地形修正
    st.write(f"守方地形修正为: <font color=red>{sf_dxxz*100}%</font>",unsafe_allow_html=True)


#分割线
st.divider()

with st.expander("（点击打开查看）神契晨曦之祝特效参考"):
    chakan_sq = pd.DataFrame(
        {"神契": ["菲依雅", "", "", "索尔", "", "", "海姆达尔", "", "", "巴德尔", "", "", "奥丁", "", "", "弗丽嘉",
                  "",
                  "", "提尔", "", "", "洛基", "", "", "维达", "", ""],
         "神祈特效": ["主动进入战斗造成魔法伤害提升2%~8%", "主动进入战斗时，目标越远伤害越高，最高提升2%~8%",
                      "主动进入战斗前未进行过移动，伤害提升2%~8%",
                      "范围伤害提升2%~8%", "进入战斗暴击率提升2%~10%", "固定伤害提升2%~10%",
                      "进入战斗遭受物理伤害降低2%~8%", "自身相邻有友军时，进入战斗遭受伤害降低1%~6%",
                      "反击伤害提升2%~10%", "遭受范围伤害降低2%~8%", "受到固定伤害降低2%~10%",
                      "主动进入战斗防御，魔防提升2%~8%", "主动进入战斗造成物理伤害提升2%~8%",
                      "范围技能命中3名及以上敌军时造成伤害提升1%~6%", "进入战斗前移动越远伤害越高，最高提升2%~8%",
                      "进入战斗时，目标越远遭受伤害越低，最多降低2%~8%", "进入战斗遭受魔法伤害降低2%~8%",
                      "部队生命低于100%时，遭受范围伤害降低2%~8%",
                      "与有弱化效果的敌军进入战斗时，造成物理伤害提升2%~8%",
                      "与克制的敌军进入战斗时，造成物理伤害提升2%~8%", "进入战斗暴击伤害提升2%~10%",
                      "与有弱化效果的敌军进入战斗时，造成魔法伤害提升2%~8%",
                      "与克制的敌军进入战斗时，造成魔法伤害提升2%~8%", "进入战斗遭受暴击率降低2%~10%",
                      "被近战攻击进入战斗时，遭受伤害降低2%~8%", "被远程攻击进入战斗时，遭受伤害降低1%~6%",
                      "进入战斗遭受暴击伤害降低2%~10%"]})
    st.dataframe(chakan_sq)

with st.expander("（点击打开查看）士兵科技参考"):
    chakan_sbkj = pd.DataFrame(
            {"士兵种类": ["步兵", "步兵", "步兵", "步兵", "步兵", "枪兵", "枪兵", "枪兵", "枪兵", "枪兵", "骑兵",
                          "骑兵", "骑兵", "骑兵", "骑兵", "飞兵", "飞兵", "飞兵", "飞兵", "水兵", "水兵", "水兵",
                          "水兵", "弓兵", "弓兵", "弓兵", "弓兵", "弓兵", "刺客", "刺客", "刺客", "刺客", "法师",
                          "法师", "法师", "法师", "僧兵", "僧兵", "僧兵", "僧兵", "魔物", "魔物", "魔物", "魔物"],
             "科技名称": ["对枪特训", "压制战法", "应急处理", "防空重甲", "孤军奋战", "对骑特训", "作战续行",
                          "反击方阵", "巩固防线", "浴血奋战", "对步特训", "集团冲锋", "高速移动", "精钢铁蹄",
                          "奔袭破阵", "先制打击", "空海奇袭", "特技飞行", "地空协同", "先制打击", "空海奇袭",
                          "水战强化", "水灵加护", "野战特训", "暗影打击", "密林游侠", "密林游侠", "闪转腾挪",
                          "野战特训", "暗影打击", "杀戮气息", "以法特训", "自我暗示", "法力虚空", "圣光护佑",
                          "聚精会神", "对魔特训", "圣光护佑", "虔诚信仰", "祛除不纯", "自我暗示", "法力虚空",
                          "暗黑力量", "污秽铠甲"],
             "科技效果": ["对枪兵士兵攻防克制修正+30%", "敌人生命百分比<=自身时,攻防+20%", "士兵大于80%血，减伤20%",
                          "被远程打,双防+20%", "身边1格没有队友,增伤30%", "对骑兵士兵攻防克制修正+30%",
                          "士兵低于70%血时,减伤20%", "被打时攻击+30%", "不站地形时,双防+20%",
                          "敌人生命百分比>=自身时,攻击+20%", "对步兵士兵攻智防克制修正+30%",
                          "身边2格有队友,攻防+20%(注意骑兵位置)", "主动进攻减伤20%", "战前每跑1格,增伤8%,最多40%",
                          "进攻被护卫时,攻防+20%", "高于80%血时,攻防+20%", "与满血敌人交战时,攻防+20%",
                          "站地形时,减伤+20%", "部队是混合部队时,双防+20%", "高于80%血时,攻防+20%",
                          "与满血敌人交战时,攻防+20%", "在水中时,增伤+30%", "在水中被打,攻击+20%,魔防+20%",
                          "站地形时，攻防+20%", "与满血敌人交战时,攻防+20%", "站地形时，增伤+30%",
                          "对飞兵士兵攻防克制修正+30%", "被近战打，双防+20%", "站地形时，攻防+20%",
                          "与满血敌人交战时,攻防+20%", "与满血敌人交战时,增伤+30%", "与法师或僧侣交战时，双防+30%",
                          "敌方有强化时，攻防+20%", "敌方有弱化时，攻防+20%", "部队满血时，减伤30%",
                          "小于等于90%血时，增伤20%", "对魔物士兵攻防克制修正+30%", "部队满血时，减伤30%",
                          "高于80%血时，增伤30%", "与混合部队交战时，攻防+20%", "敌方有强化时，攻防+20%",
                          "敌方有弱化时，攻防+20%", "自身有弱化时，增伤30%",
                          "常驻双防+20%，但与魔物或僧侣交战时，双防克制修正-16%"]})
    st.dataframe(chakan_sbkj)

#分割线
st.divider()

#定义兵打兵单段伤害 bdb_dd_sh
#定义兵打兵单段暴击伤害 bdb_ddbj_sh
#定义兵打英雄单段伤害 bdyx_dd_sh
#定义兵打英雄单段暴击伤害 bdyx_ddbj_sh

if sbsh_lx == "物理":
#计算兵打兵物理伤害
    bdb_dd_sh = (gf_sbgj*(1+gf_sbdsb_gzkzxs) - sf_sbfy*(1+sf_sbdsb_sfkzxs+sf_dxxz)*(1-gf_sb_wsfy)) * gf_sbjnbl * (1+gf_sb_tyzs-sf_sb_wl_tyjs) * (1+gf_sb_jnzs-sf_sb_jnjs) * (1+gf_sb_yczs-sf_sb_ycjs) * (1+gf_sb_qtzs-sf_sb_qtjs) * 0.5
    bdb_ddbj_sh = bdb_dd_sh * (1.3+gf_sb_bs-sf_sb_jbs)
#计算兵打英雄物理伤害
    bdyx_dd_sh = (gf_sbgj*(1+gf_sbdyx_gzkzxs) - sf_yxfy*(1+sf_yxdsb_sfkzxs+sf_dxxz)*(1-gf_sb_wsfy)) * gf_sbjnbl * (1+gf_sb_tyzs- sf_yx_wl_tyjs) * (1+gf_sb_jnzs-sf_yx_jnjs) * (1+gf_sb_yczs-sf_yx_ycjs) * (1+gf_sb_qtzs-sf_yx_qtjs) * 0.5
    bdyx_ddbj_sh = bdb_dd_sh * (1.3+gf_sb_bs-sf_yx_jbs)
else:
#计算兵打兵魔法伤害
    bdb_dd_sh = (gf_sbgj*(1+gf_sbdsb_gzkzxs) - sf_sbmf*(1+sf_sbdsb_sfkzxs+sf_dxxz)*(1-gf_sb_wsfy)) * gf_sbjnbl * (1+gf_sb_tyzs-sf_sb_mf_tyjs) * (1+gf_sb_jnzs-sf_sb_jnjs) * (1+gf_sb_yczs-sf_sb_ycjs) * (1+gf_sb_qtzs-sf_sb_qtjs) * 0.5
    bdb_ddbj_sh = bdb_dd_sh * (1.3+gf_sb_bs-sf_sb_jbs)
#计算兵打英雄魔法伤害
    bdyx_dd_sh = (gf_sbgj*(1+gf_sbdyx_gzkzxs) - sf_yxmf*(1+sf_yxdsb_sfkzxs+sf_dxxz)*(1-gf_sb_wsfy)) * gf_sbjnbl * (1+gf_sb_tyzs- sf_yx_mf_tyjs) * (1+gf_sb_jnzs-sf_yx_jnjs) * (1+gf_sb_yczs-sf_yx_ycjs) * (1+gf_sb_qtzs-sf_yx_qtjs) * 0.5
    bdyx_ddbj_sh = bdb_dd_sh * (1.3+gf_sb_bs-sf_yx_jbs)

#定义英雄打兵单段伤害 yxdb_dd_sh
#定义英雄打兵单段暴击伤害 yxdb_ddbj_sh
#定义英雄打英雄单段伤害 yxdyx_dd_sh
#定义英雄打英雄单段暴击伤害 yxdyx_ddbj_sh

if yxsh_lx == "物理":
#计算英雄打兵物理伤害
    yxdb_dd_sh = (gf_yxgj*(1+gf_yxdsb_gzkzxs) - sf_sbfy*(1+sf_sbdyx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)) * gf_yxjnbl * (1+gf_yx_tyzs-sf_sb_wl_tyjs) * (1+gf_yx_jnzs-sf_sb_jnjs) * (1+gf_yx_yczs-sf_sb_ycjs) * (1+gf_yx_qtzs-sf_sb_qtjs) * 0.5
    yxdb_ddbj_sh = yxdb_dd_sh * (1.3+gf_yx_bs-sf_sb_jbs)
#计算英雄打英雄物理伤害
    yxdyx_dd_sh = (gf_yxgj*(1+gf_yxdyx_gzkzxs) - sf_yxfy*(1+sf_yxdyx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)) * gf_yxjnbl * (1+gf_yx_tyzs- sf_yx_wl_tyjs) * (1+gf_yx_jnzs-sf_yx_jnjs) * (1+gf_yx_yczs-sf_yx_ycjs) * (1+gf_yx_qtzs-sf_yx_qtjs) * 0.5
    yxdyx_ddbj_sh = yxdyx_dd_sh * (1.3+gf_yx_bs-sf_yx_jbs)
else:
#计算英雄打兵魔法伤害
    yxdb_dd_sh = (gf_yxzl*(1+gf_yxdsb_gzkzxs) - sf_sbmf*(1+sf_sbdyx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)) * gf_yxjnbl * (1+gf_yx_tyzs-sf_sb_mf_tyjs) * (1+gf_yx_jnzs-sf_sb_jnjs) * (1+gf_yx_yczs-sf_sb_ycjs) * (1+gf_yx_qtzs-sf_sb_qtjs) * 0.5
    yxdb_ddbj_sh = yxdb_dd_sh * (1.3+gf_yx_bs-sf_sb_jbs)
#计算英雄打英雄魔法伤害
    yxdyx_dd_sh = (gf_yxzl*(1+gf_yxdyx_gzkzxs) - sf_yxmf*(1+sf_yxdyx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)) * gf_yxjnbl * (1+gf_yx_tyzs- sf_yx_mf_tyjs) * (1+gf_yx_jnzs-sf_yx_jnjs) * (1+gf_yx_yczs-sf_yx_ycjs) * (1+gf_yx_qtzs-sf_yx_qtjs) * 0.5
    yxdyx_ddbj_sh = yxdyx_dd_sh * (1.3+gf_yx_bs-sf_yx_jbs)

column4, column5, column6 = st.columns([1,0.1,1])

with column4:
    st.markdown(f"##### 兵打兵单段伤害为 <strong><span style='color:blue;font-size:25px;'>{round(bdb_dd_sh, 2)}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 兵打兵暴击单段伤害为 <strong><span style='color:orange;font-size:25px;'>{round(bdb_ddbj_sh, 2)}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 英雄打兵单段伤害为 <strong><span style='color:blue;font-size:25px;'>{round(yxdb_dd_sh, 2)}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 英雄打兵暴击单段伤害为 <strong><span style='color:orange;font-size:25px;'>{round(yxdb_ddbj_sh, 2)}</span></strong>", unsafe_allow_html=True)

with column6:
    st.markdown(f"##### 兵打英雄单段伤害为 <strong><span style='color:green;font-size:25px;'>{round(bdyx_dd_sh, 2)}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 兵打英雄暴击单段伤害为 <strong><span style='color:orange;font-size:25px;'>{round(bdyx_ddbj_sh, 2)}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 英雄打英雄单段伤害为 <strong><span style='color:green;font-size:25px;'>{round(yxdyx_dd_sh, 2)}</span></strong>", unsafe_allow_html=True)
    st.markdown(f"##### 英雄打英雄暴击单段伤害为 <strong><span style='color:orange;font-size:25px;'>{round(yxdyx_ddbj_sh, 2)}</span></strong>", unsafe_allow_html=True)

#分割线
st.divider()

column66, column67, column68 = st.columns([1,0.1,1])
#判断是否暴击
with column66:
    bdb_sfbj = st.checkbox("兵打兵 是否暴击")
    bdyx_sfbj = st.checkbox("兵打英雄 是否暴击")
with column68:
    yxdb_sfbj = st.checkbox("英雄打兵 是否暴击")
    yxdyx_sfbj = st.checkbox("英雄打英雄 是否暴击")

if bdb_sfbj:
    sj_bdb_sh = round(bdb_ddbj_sh)
else:
    sj_bdb_sh = round(bdb_dd_sh)

if bdb_sfbj:
    sj_bdyx_sh = round(bdyx_ddbj_sh)
else:
    sj_bdyx_sh = round(bdyx_dd_sh)

if yxdb_sfbj:
    sj_yxdb_sh = round(yxdb_ddbj_sh)
else:
    sj_yxdb_sh = round(yxdb_dd_sh)

if yxdyx_sfbj:
    sj_yxdyx_sh = round(yxdyx_ddbj_sh)
else:
    sj_yxdyx_sh = round(yxdyx_dd_sh)

if sj_bdb_sh < 1:
    sj_bdb_sh = 1
if sj_bdyx_sh < 1:
    sj_bdyx_sh = 1
if sj_yxdb_sh < 1:
    sj_yxdb_sh = 1
if sj_yxdyx_sh < 1:
    sj_yxdyx_sh = 1

#分割线
st.divider()

#定义兵打兵 攻防差bdb_gfc 通用增减%bdb_tyzj 技能增减%bdb_jnzj 远程增减%bdb_yczj 其他增减%bdb_qtzj 技能倍率bdb_jnbl
#定义兵打英雄 攻防差bdyx_gfc 通用增减%bdyx_tyzj 技能增减%bdyx_jnzj 远程增减%bdyx_yczj 其他增减%bdyx_qtzj 技能倍率bdyx_jnbl
if sbsh_lx == "物理":
    bdb_gfc = gf_sbgj*(1+gf_sbdsb_gzkzxs) - sf_sbfy*(1+sf_sbdsb_sfkzxs+sf_dxxz)*(1-gf_sb_wsfy)
    bdb_tyzj = (gf_sb_tyzs - sf_sb_wl_tyjs)*100
    bdb_jnzj = (gf_sb_jnzs - sf_sb_jnjs)*100
    bdb_yczj = (gf_sb_yczs - sf_sb_ycjs)*100
    bdb_qtzj = (gf_sb_qtzs - sf_sb_qtjs)*100
    bdb_jnbl = gf_sbjnbl
    bdyx_gfc = gf_sbgj*(1+gf_sbdyx_gzkzxs) - sf_yxfy*(1+sf_yxdsb_sfkzxs+sf_dxxz)*(1-gf_sb_wsfy)
    bdyx_tyzj = (gf_sb_tyzs- sf_yx_wl_tyjs)*100
    bdyx_jnzj = (gf_sb_jnzs-sf_yx_jnjs)*100
    bdyx_yczj = (gf_sb_yczs-sf_yx_ycjs)*100
    bdyx_qtzj = (gf_sb_qtzs-sf_yx_qtjs)*100
    bdyx_jnbl = gf_sbjnbl
else:
    bdb_gfc = gf_sbgj*(1+gf_sbdsb_gzkzxs) - sf_sbmf*(1+sf_sbdsb_sfkzxs+sf_dxxz)*(1-gf_sb_wsfy)
    bdb_tyzj = (gf_sb_tyzs-sf_sb_mf_tyjs)*100
    bdb_jnzj = (gf_sb_jnzs-sf_sb_jnjs)*100
    bdb_yczj = (gf_sb_yczs-sf_sb_ycjs)*100
    bdb_qtzj = (gf_sb_qtzs-sf_sb_qtjs)*100
    bdb_jnbl = gf_sbjnbl
    bdyx_gfc = gf_sbgj*(1+gf_sbdyx_gzkzxs) - sf_yxmf*(1+sf_yxdsb_sfkzxs+sf_dxxz)*(1-gf_sb_wsfy)
    bdyx_tyzj = (gf_sb_tyzs- sf_yx_mf_tyjs)*100
    bdyx_jnzj = (gf_sb_jnzs-sf_yx_jnjs)*100
    bdyx_yczj = (gf_sb_yczs-sf_yx_ycjs)*100
    bdyx_qtzj = (gf_sb_qtzs-sf_yx_qtjs)*100
    bdyx_jnbl = gf_sbjnbl
#定义英雄打兵 攻防差yxdb_gfc 通用增减%yxdb_tyzj 技能增减%yxdb_jnzj 远程增减%yxdb_yczj 其他增减%yxdb_qtzj 技能倍率yxdb_jnbl
#定义英雄打英雄 攻防差yxdyx_gfc 通用增减%yxdyx_tyzj 技能增减%yxdyx_jnzj 远程增减%yxdyx_yczj 其他增减%yxdyx_qtzj 技能倍率yxdyx_jnbl
if yxsh_lx == "物理":
    yxdb_gfc = gf_yxgj*(1+gf_yxdsb_gzkzxs) - sf_sbfy*(1+sf_sbdyx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)
    yxdb_tyzj = gf_yx_tyzs-sf_sb_wl_tyjs
    yxdb_jnzj = gf_yx_jnzs-sf_sb_jnjs
    yxdb_yczj = gf_yx_yczs-sf_sb_ycjs
    yxdb_qtzj = gf_yx_qtzs-sf_sb_qtjs
    yxdb_jnbl = gf_yxjnbl
    yxdyx_gfc = gf_yxgj*(1+gf_yxdyx_gzkzxs) - sf_yxfy*(1+sf_yxdyx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)
    yxdyx_tyzj = gf_yx_tyzs- sf_yx_wl_tyjs
    yxdyx_jnzj = gf_yx_jnzs-sf_yx_jnjs
    yxdyx_yczj = gf_yx_yczs-sf_yx_ycjs
    yxdyx_qtzj = gf_yx_qtzs-sf_yx_qtjs
    yxdyx_jnbl = gf_yxjnbl
else:
    yxdb_gfc = gf_yxzl*(1+gf_yxdsb_gzkzxs) - sf_sbmf*(1+sf_sbdyx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)
    yxdb_tyzj = gf_yx_tyzs-sf_sb_mf_tyjs
    yxdb_jnzj = gf_yx_jnzs-sf_sb_jnjs
    yxdb_yczj = gf_yx_yczs-sf_sb_ycjs
    yxdb_qtzj = gf_yx_qtzs-sf_sb_qtjs
    yxdb_jnbl = gf_yxjnbl
    yxdyx_gfc = gf_yxzl*(1+gf_yxdyx_gzkzxs) - sf_yxmf*(1+sf_yxdyx_sfkzxs+sf_dxxz)*(1-gf_yx_wsfy)
    yxdyx_tyzj = gf_yx_tyzs- sf_yx_mf_tyjs
    yxdyx_jnzj = gf_yx_jnzs-sf_yx_jnjs
    yxdyx_yczj = gf_yx_yczs-sf_yx_ycjs
    yxdyx_qtzj = gf_yx_qtzs-sf_yx_qtjs
    yxdyx_jnbl = gf_yxjnbl

with st.expander("（点击打开查看）战斗攻防差与增减伤关系（注：已考虑克制系数、无视防御、地形修正）"):
    chakan_gfczjs = pd.DataFrame({"攻守方": ["兵打兵","兵打英雄","英雄打兵","英雄打英雄"],"攻防差": [bdb_gfc,bdyx_gfc,yxdb_gfc,yxdyx_gfc],"通用增减%": [bdb_tyzj,bdyx_tyzj,yxdb_tyzj,yxdyx_tyzj],"技能增减%": [bdb_jnzj,bdyx_jnzj,yxdb_jnzj,yxdyx_jnzj],"远程增减%": [bdb_yczj,bdyx_yczj,yxdb_yczj,yxdyx_yczj],"其他增减%": [bdb_qtzj,bdyx_qtzj,yxdb_qtzj,yxdyx_qtzj],"技能倍率": [bdb_jnbl,bdyx_jnbl,yxdb_jnbl,yxdyx_jnbl],"单段": [bdb_dd_sh,bdyx_dd_sh,yxdb_dd_sh,yxdyx_dd_sh],"暴击单段": [bdb_ddbj_sh,bdyx_ddbj_sh,yxdb_ddbj_sh,yxdyx_ddbj_sh]})
    # 使用 style.format 将所有列格式化为一位小数
    chakan_gfczjs = chakan_gfczjs.style.format({
        "攻防差": "{:.1f}",
        "通用增减%": "{:.1f}",
        "技能增减%": "{:.1f}",
        "远程增减%": "{:.1f}",
        "其他增减%": "{:.1f}",
        "技能倍率": "{:.1f}",
        "单段": "{:.1f}",
        "暴击单段": "{:.1f}"
    })
    # 使用 st.dataframe 显示带有格式化的表格
    st.dataframe(chakan_gfczjs)

#分割线
st.divider()

st.markdown(f"<strong><span style='color:red;font-size:25px;'>以下即将进行段数分配战斗模拟</span></strong>", unsafe_allow_html=True)

sdsr_pd = st.checkbox("关联读取以上单段伤害计算结果 (想手动输入单段伤害 就取消勾选)", value=True)

if sdsr_pd:
    soldier_to_soldier_damage = sj_bdb_sh
    soldier_to_hero_damage = sj_bdyx_sh
    hero_to_soldier_damage = sj_yxdb_sh
    hero_to_hero_damage = sj_yxdyx_sh
else:
    soldier_to_soldier_damage = round(st.number_input("士兵打士兵的单段伤害", min_value=1,value=1))
    soldier_to_hero_damage = round(st.number_input("士兵打英雄的单段伤害", min_value=1,value=1))
    hero_to_soldier_damage = round(st.number_input("英雄打士兵的单段伤害", min_value=1,value=1))
    hero_to_hero_damage = round(st.number_input("英雄打英雄的单段伤害", min_value=1,value=1))


#分割线
st.divider()

# 攻方士兵是否满血选择
attacker_full_health = st.checkbox("攻方士兵是否满血",value=True)

if attacker_full_health:
    attacker_soldier_count = 10  # 满血时固定为10
    st.write("攻方士兵当前数量: 10（满血）")
else:
    attacker_soldier_count = st.number_input("攻方士兵当前数量", min_value=0, value=10)  # 不满血时用户可以输入数量

#分割线
st.divider()

# 定义每只守方士兵的最大血量
defender_soldier_max_hp_per_unit = st.text_input("每只守方士兵的最大血量", "1")
defender_soldier_max_hp_per_unit = mb_shuru(defender_soldier_max_hp_per_unit)
# 守方每只守方士兵的最大血量
if defender_soldier_max_hp_per_unit <= 1:
    efender_soldier_max_hp_per_unit = 1
else:
    defender_soldier_max_hp_per_unit = round(defender_soldier_max_hp_per_unit)
st.write(f"每只兵: {defender_soldier_max_hp_per_unit}")

# 守方士兵是否满血选择
defender_full_health = st.checkbox("守方士兵是否满血",value=True)

if defender_full_health:
    defender_soldier_count = 10  # 满血时固定为10
    defender_soldier_hp = defender_soldier_max_hp_per_unit * 10  # 总血量为最大血量 * 10
    st.write(f"守方士兵当前总血量: {defender_soldier_hp}（满血）")
else:
    defender_soldier_hp = st.text_input("守方士兵当前总血量", "0") # 不满血时用户可以输入总血量
    defender_soldier_hp = mb_shuru(defender_soldier_hp)
    # 守方士兵当前血量最小为0
    if defender_soldier_hp <= 0:
        defender_soldier_hp = 0
    else:
        defender_soldier_hp = round(defender_soldier_hp)
    defender_soldier_count = math.ceil(defender_soldier_hp / defender_soldier_max_hp_per_unit)  # 计算守方士兵数量

#分割线
st.divider()

#定义守方英雄当前血量
defender_hero_hp = st.text_input("守方英雄当前血量", "1")
defender_hero_hp = mb_shuru(defender_hero_hp)
# 守方英雄当前血量最小为1
if defender_hero_hp <= 1:
    defender_hero_hp = 1
else:
    defender_hero_hp = round(defender_hero_hp)

#分割线
st.divider()

#定义护盾值
hudun_hp = st.text_input("护盾值", "0")
hudun_hp = mb_shuru(hudun_hp)
# 守方英雄当前血量最小为1
if hudun_hp <= 1:
    hudun_hp = 1
else:
    hudun_hp = round(hudun_hp)

#分割线
st.divider()

# 士兵出手的最大段数（按攻方士兵数量和每只士兵的2段攻击计算）
attacker_soldier_max_segments = attacker_soldier_count * 2

sb_dsdspd = st.checkbox("士兵是否有真正的段数丢失（有就勾选）")
if sb_dsdspd:
    attacker_soldier_dsds = st.number_input("士兵丢失段数", min_value=0, max_value=attacker_soldier_max_segments,value=0)
    attacker_soldier_max_segments = attacker_soldier_max_segments - attacker_soldier_dsds

# 用户选择士兵优先出手的段数
st.write(f"士兵出手的段数最大参考值: {attacker_soldier_max_segments}")
if attacker_soldier_count == 0:
    soldier_to_soldier_priority_segments = 0
else:
    soldier_to_soldier_priority_segments = st.slider("请选择士兵优先英雄出手的段数（根据英雄出手速度判断）", min_value=0, max_value=attacker_soldier_max_segments, value=attacker_soldier_max_segments)

# 初始化剩余士兵段数、英雄出手段数
remaining_soldier_segments = attacker_soldier_max_segments - soldier_to_soldier_priority_segments
hero_segments = gf_yx_gjds

# 初始化守方士兵和英雄的剩余血量
defender_soldier_remaining_hp = defender_soldier_hp
defender_hero_remaining_hp = defender_hero_hp

# 初始化剩余护盾值
hudun_remaining_hp = hudun_hp #用护盾值这个变更来记录护盾值的变化

# 初始化护盾是否已经被士兵使用的标志
shield_used = False

# 初始化士兵和英雄的击杀计数
soldier_killed_by_soldier = 0 #用于记录士兵杀死多少只士兵
soldier_killed_by_hero = 0 #用于记录英雄杀死多少只士兵

# 定义守方士兵状态判断函数（计算首只士兵血量，剩余士兵数）
def calculate_defender_soldier_status(defender_soldier_remaining_hp, defender_soldier_max_hp_per_unit):
    remaining_hp_after_full_soldiers = defender_soldier_remaining_hp % defender_soldier_max_hp_per_unit
    if remaining_hp_after_full_soldiers > 0:
        first_soldier_hp = remaining_hp_after_full_soldiers
        defender_soldier_count = math.floor(defender_soldier_remaining_hp / defender_soldier_max_hp_per_unit) + 1
    else:
        first_soldier_hp = defender_soldier_max_hp_per_unit
        defender_soldier_count = defender_soldier_remaining_hp // defender_soldier_max_hp_per_unit
    return first_soldier_hp, defender_soldier_count

#函数阅读理解
# defender_soldier_remaining_hp 士兵当前总血量
# defender_soldier_max_hp_per_unit 每只士兵总血量
# remaining_hp_after_full_soldiers 士兵当前总血量/每只士兵总血量 算出来的余数，用于判断首个士兵是不是残血，如果是残血，会赋值给首个士兵
# first_soldier_hp 最前面那只士兵的血量，如果是残血士兵，会赋值为 remaining_hp_after_full_soldiers，如果是满血士兵，会赋值为defender_soldier_max_hp_per_unit
# defender_soldier_count 当前士兵的数量，利用math.floor向下取整后，加1
# 函数最后返回的是 first_soldier_hp最前面那只士兵的血量 和 defender_soldier_count当前士兵的数量

# ------------------------------
# 阶段1：士兵优先出手打士兵
# ------------------------------

# 计算第一只士兵的血量（计算是否第一只士兵是残血士兵）

# 计算当前守方士兵状态
first_soldier_hp, defender_soldier_count = calculate_defender_soldier_status(defender_soldier_remaining_hp, defender_soldier_max_hp_per_unit)
# 利用函数得到第一阶段时 第一只士兵的血量first_soldier_hp，以及当前士兵的数量defender_soldier_count

if first_soldier_hp > 0 and defender_soldier_remaining_hp > 0: #当士兵血量不为0即有士兵时
    shield_used = True #使用护盾
    first_soldier_hp_hudun = first_soldier_hp + hudun_remaining_hp #将护盾加到第1只士兵身上

# 分割线
st.divider()

# 输出第1只士兵信息（用于调试）
st.write(f"士兵承伤阶段1 - 兵打兵 - 第1只士兵血量: {first_soldier_hp}")

# 处理士兵优先出手段数
soldier_to_soldier_segments_used = 0 #用一个变量从0开始记录1阶段的士兵兵打兵段数

# 处理第1只士兵（如果存在）
if first_soldier_hp > 0 and defender_soldier_remaining_hp > 0: #当士兵血量不为0即有士兵时
    segments_needed_to_kill_last_soldier = math.ceil(first_soldier_hp_hudun / soldier_to_soldier_damage) #soldier_to_soldier_damage是兵打兵的单段伤害，这个公式是算出第1只士兵向上取整需要多少段能杀，segments_needed_to_kill_last_soldier就是算多少段能杀，护盾值加在第一个士兵上
    if soldier_to_soldier_priority_segments >= segments_needed_to_kill_last_soldier: #soldier_to_soldier_priority_segments是士兵优先英雄出手的段数，之前用滑动条选择的，判断如果大于 等于 能杀第1只士兵的段数，判断击杀第1只兵
        # 判断击杀第1只士兵
        soldier_to_soldier_priority_segments -= segments_needed_to_kill_last_soldier #士兵优先出手的段数 - 击杀第1只士兵消耗的段数 = 剩余的段数（但这里总感觉应该用新变量来记录）
        defender_soldier_remaining_hp -= first_soldier_hp #当前士兵总血量 - 第1只士兵的血量 = 当前士兵剩余血量（但这里总感觉应该用新变量来记录）
        soldier_to_soldier_segments_used += segments_needed_to_kill_last_soldier #soldier_to_soldier_segments_used 是个之前定义的新变更，用来记录第一阶段使用了多少兵打兵段数。这里是把打第1只士兵消耗的段数进行记录
        first_soldier_hp = 0  # 第1只士兵已被杀死
        soldier_killed_by_soldier += 1 # 记录士兵杀死1只士兵
        hudun_remaining_hp = 0 # 剩余护盾值为0
    else:
        # 第1只士兵未被打死
        defender_soldier_remaining_hp = min(defender_soldier_remaining_hp,defender_soldier_remaining_hp + hudun_remaining_hp - soldier_to_soldier_priority_segments * soldier_to_soldier_damage) #当前士兵总血量 - 士兵优先英雄出手的段数（就是之前用滑段选择的）*兵打兵的单段伤害 = 计算出当前士兵总血量剩余血量
        first_soldier_hp = min(first_soldier_hp , first_soldier_hp_hudun - soldier_to_soldier_priority_segments * soldier_to_soldier_damage) #第1只士兵血量 - 士兵优先英雄出手的段数（就是之前用滑段选择的）*兵打兵的单段伤害 = 第1士兵目前剩余的血量，这里要考虑护盾值
        soldier_to_soldier_segments_used += soldier_to_soldier_priority_segments #soldier_to_soldier_segments_used 是个之前定义的新变更，用来记录第一阶段使用了多少兵打兵段数，这里是把打第1只士兵消耗的段数进行记录
        hudun_remaining_hp = max(0 , hudun_remaining_hp - soldier_to_soldier_priority_segments * soldier_to_soldier_damage) # 计算剩余护盾值
        soldier_to_soldier_priority_segments = 0 #这里记录soldier_to_soldier_priority_segments 士兵优先英雄出手的段数为0了，消耗光了
        first_soldier_hp_hudun = first_soldier_hp + hudun_remaining_hp  # 再次将护盾加到第1只士兵身上并记录

# 这个阶段以后，护盾使用过（即不能再给英雄使用），而且护盾值消耗了一部分，有可能为0

# 处理从第2只士兵开始的满血士兵的承伤
for _ in range(defender_soldier_count - 1):  # 忽略已处理的第1只士兵
    if soldier_to_soldier_priority_segments == 0 or defender_soldier_remaining_hp <= 0: # 做1个判断，若士兵优先英雄出手的段数为0即已经用完，或者当前士兵总血量为0即没有士兵了，就跳出循环
        break
    current_soldier_hp = defender_soldier_max_hp_per_unit # current_soldier_hp是每只满血士兵血量，等于每只守方士兵最大血量defender_soldier_max_hp_per_unit
    segments_needed_to_kill_soldier = math.ceil(current_soldier_hp / soldier_to_soldier_damage) #士兵被击杀的段数segments_needed_to_kill_soldier = 每只满血士兵血量current_soldier_hp / 兵打兵单段伤害soldier_to_soldier_damage 向上取整

    if soldier_to_soldier_priority_segments >= segments_needed_to_kill_soldier: #剩余的段数soldier_to_soldier_priority_segments大于等于击杀需要的段数，判断杀死
        # 杀死当前士兵
        soldier_to_soldier_priority_segments -= segments_needed_to_kill_soldier #计算杀死后，消耗的段数
        defender_soldier_remaining_hp -= current_soldier_hp #计算杀死后，当前士兵剩余的总血量
        soldier_to_soldier_segments_used += segments_needed_to_kill_soldier #继续累积去记录消耗的兵打兵段数
        soldier_killed_by_soldier += 1 # 记录累计士兵杀死士兵的个数
    else:
        # 当前士兵未被打死
        defender_soldier_remaining_hp -= soldier_to_soldier_priority_segments * soldier_to_soldier_damage #计算未被杀死时，当前士兵剩余的总血量
        soldier_to_soldier_segments_used += soldier_to_soldier_priority_segments #继续累积去记录消耗的兵打兵段数
        soldier_to_soldier_priority_segments = 0 #这里记录soldier_to_soldier_priority_segments 士兵优先英雄出手的段数为0了，消耗光了
        break #段数用完，跳出循环了

# ------------------------------
# 处理士兵打英雄的段数，加入鞭尸机制
# ------------------------------

# 初始化鞭尸丢失段数
soldier_to_hero_lost_segments_1 = 0 #用一个变更记录鞭尸丢失的段数
soldier_to_hero_segments_used_1 = 0 #士兵打英雄的实际作用段数（未丢失）第1阶段

if not shield_used and defender_soldier_remaining_hp <= 0: #如果护盾没被使用且没有士兵
    defender_hero_remaining_hp_hudun = hudun_remaining_hp + defender_hero_remaining_hp
else:
    defender_hero_remaining_hp_hudun =  defender_hero_remaining_hp

if  soldier_to_soldier_priority_segments > 0 :
    soldier_to_hero_segments = soldier_to_soldier_priority_segments
    # 计算守方英雄剩余血量与实际作用段数
    if defender_hero_remaining_hp > 0 and defender_soldier_remaining_hp == 0: #如果守方英雄剩余血量大于0且没有士兵了， 若士兵段数还有剩余且守方士兵已被打光，则剩余段数打英雄
        segments_needed_to_kill_hero = math.ceil(defender_hero_remaining_hp_hudun / soldier_to_hero_damage) #计算守方英雄的剩余血量需要多少段兵打英雄能杀掉
        if soldier_to_hero_segments >= segments_needed_to_kill_hero: #如果兵打英雄的段数能杀死英雄
            # 杀死英雄，剩余的段数被鞭尸丢失
            soldier_to_hero_segments_used_1 = segments_needed_to_kill_hero #定义soldier_to_hero_segments_used为士兵打英雄的真实段数
            soldier_to_hero_lost_segments_1 = soldier_to_hero_segments - segments_needed_to_kill_hero #计算鞭尸丢失的段数
            defender_hero_remaining_hp = 0 #守方英雄剩余血量为0
            if not shield_used:
                hudun_remaining_hp = 0  # 剩余护盾值为0
        else:
            # 英雄未被打死，全部段数都生效
            soldier_to_hero_segments_used_1 = soldier_to_hero_segments #定义soldier_to_hero_segments_used为士兵打英雄的真实段数，英雄未死全部都算
            soldier_to_hero_lost_segments_1 = 0 #计算鞭尸丢失的段数为0
            defender_hero_remaining_hp = min(defender_hero_remaining_hp , defender_hero_remaining_hp_hudun - soldier_to_hero_segments * soldier_to_hero_damage) #计算守方英雄的剩余血量
            if not shield_used:
                hudun_remaining_hp = max(0 , hudun_remaining_hp - soldier_to_hero_segments * soldier_to_hero_damage) # 计算剩余护盾值
                defender_hero_remaining_hp_hudun = hudun_remaining_hp + defender_hero_remaining_hp
    elif defender_hero_remaining_hp <= 0 and defender_soldier_remaining_hp <= 0:     # 如果英雄已经死亡，则所有段数都被鞭尸丢失
        soldier_to_hero_lost_segments_1 = soldier_to_hero_segments #计算鞭尸丢失的段数全丢了
        soldier_to_hero_segments_used_1 = 0 #士兵打英雄的真实段数为0
else:
    soldier_to_hero_segments_used_1 = 0

# ------------------------------
# 阶段2：英雄出手打士兵
# ------------------------------

# 重新计算守方士兵状态
first_soldier_hp, defender_soldier_count = calculate_defender_soldier_status(defender_soldier_remaining_hp, defender_soldier_max_hp_per_unit)
# 利用函数得到第二阶段时，排最前面的士兵的血量first_soldier_hp，以及当前士兵的数量defender_soldier_count

if first_soldier_hp > 0 and defender_soldier_remaining_hp > 0: #当排头士兵血量不为0且有士兵时
    if hudun_remaining_hp > 0: #护盾值不为0，把护盾加到排头士兵上
        first_soldier_hp_hudun = first_soldier_hp + hudun_remaining_hp
    else:
        first_soldier_hp_hudun = first_soldier_hp

# 输出排头士兵信息（用于调试）
st.write(f"士兵承伤阶段2 - 英雄打兵 - 排头士兵血量: {first_soldier_hp}")

hero_to_soldier_segments_used = 0 #用一个变量从0开始记录2阶段的英雄打兵的段数

# 处理排头士兵
if first_soldier_hp > 0 and defender_soldier_remaining_hp > 0: #当排头士兵血量不为0且有士兵时
    segments_needed_to_kill_last_soldier = math.ceil(first_soldier_hp_hudun / hero_to_soldier_damage) #计算杀死排头士兵需要多少段英雄打兵的段数
    if hero_segments >= segments_needed_to_kill_last_soldier: #判断英雄段数是否能杀排头士兵，hero_segments是英雄出手的段数
        # 杀死排头士兵
        hero_segments -= segments_needed_to_kill_last_soldier #计算杀死排头士兵后，英雄剩余的段数
        defender_soldier_remaining_hp -= first_soldier_hp #计算杀死排头士兵后，当前士兵总血量剩多少
        hero_to_soldier_segments_used += segments_needed_to_kill_last_soldier #累计记录英雄打兵消耗的段数
        first_soldier_hp = 0 #将排头士兵血量定为0
        soldier_killed_by_hero += 1 # 记录英雄杀死1只士兵
        hudun_remaining_hp = 0  # 剩余护盾值为0
    else:
        # 排头士兵未被打死
        defender_soldier_remaining_hp = min(defender_soldier_remaining_hp,defender_soldier_remaining_hp + hudun_remaining_hp - hero_segments * hero_to_soldier_damage) #当前士兵总血量剩多少
        first_soldier_hp = min(first_soldier_hp, first_soldier_hp_hudun - hero_segments * hero_to_soldier_damage) #计算排头士兵血量剩多少
        hero_to_soldier_segments_used += hero_segments #累计记录英雄打兵消耗的段数，没打死就全记录
        hudun_remaining_hp = max(0,hudun_remaining_hp - hero_segments * hero_to_soldier_damage)  # 计算剩余护盾值
        hero_segments = 0 #英雄出手段数用完了
        first_soldier_hp_hudun = first_soldier_hp + hudun_remaining_hp #将护盾值继续加在排头士兵身上

# 这一阶段完后，有可能剩余护盾，也有可能为0，护盾此时已被使用过

    # 处理满血士兵
for _ in range(defender_soldier_count - 1): #忽略已处理的排头士兵
    if hero_segments == 0 or defender_soldier_remaining_hp <= 0: #英雄出手段数用完或当前士兵总血量为0即没有士兵了，跳出循环
        break
    current_soldier_hp = defender_soldier_max_hp_per_unit #current_soldier_hp是每只满血士兵血量，等于每只守方士兵最大血量defender_soldier_max_hp_per_unit
    segments_needed_to_kill_soldier = math.ceil(current_soldier_hp / hero_to_soldier_damage) #计算一只满血的士兵要消耗英雄打兵多少段

    if hero_segments >= segments_needed_to_kill_soldier: #如果英雄段数足够杀死一只满血士兵
        hero_segments -= segments_needed_to_kill_soldier #计算杀死这只士兵后，英雄剩余的段数
        defender_soldier_remaining_hp -= current_soldier_hp #计算杀死这只士兵后，当前士兵总血量剩多少
        hero_to_soldier_segments_used += segments_needed_to_kill_soldier #累计记录英雄打兵消耗的段数
        soldier_killed_by_hero += 1 # 记录累计英雄杀死士兵的个数
    else:
        defender_soldier_remaining_hp -= hero_segments * hero_to_soldier_damage #当前士兵总血量剩多少
        hero_to_soldier_segments_used += hero_segments #累计记录英雄打兵消耗的段数，没打死就全记录
        hero_segments = 0 #英雄出手段数用完了
        break

# 若英雄出手段数还有剩余且守方士兵已被打光，则剩余段数打英雄

if not shield_used and defender_soldier_remaining_hp <= 0: #如果护盾没被使用且没有士兵
    if hudun_remaining_hp > 0:
        defender_hero_remaining_hp_hudun = hudun_remaining_hp + defender_hero_remaining_hp
    else:
        defender_hero_remaining_hp_hudun =  defender_hero_remaining_hp

if hero_segments > 0:
    if defender_hero_remaining_hp > 0 and defender_soldier_remaining_hp <= 0: #如果守方英雄剩余血量大于0且没有士兵了
        hero_to_hero_segments = hero_segments  # hero_to_hero_segments表示英雄打英雄的段数，这里是将剩余的第二阶段的英雄段数全赋值给英雄打英雄
        defender_hero_remaining_hp = max(0,min(defender_hero_remaining_hp , defender_hero_remaining_hp_hudun - hero_to_hero_segments*hero_to_hero_damage)) #计算英雄打英雄后，守方英雄剩余的当前血量
        hudun_remaining_hp = max(0, hudun_remaining_hp - hero_to_hero_segments * hero_to_hero_damage)  # 计算剩余护盾值
        defender_hero_remaining_hp_hudun = hudun_remaining_hp + defender_hero_remaining_hp
    elif defender_hero_remaining_hp <= 0 and defender_soldier_remaining_hp <= 0: #如果守方英雄已经死了
        hero_to_hero_segments = 0 #英雄段数丢失
else:
    hero_to_hero_segments = 0

# ------------------------------
# 阶段3：剩余士兵出手打士兵
# ------------------------------

# 重新计算守方士兵状态
first_soldier_hp, defender_soldier_count = calculate_defender_soldier_status(defender_soldier_remaining_hp, defender_soldier_max_hp_per_unit)
# 利用函数得到第二阶段时，排最前面的士兵的血量first_soldier_hp，以及当前士兵的数量defender_soldier_count

if first_soldier_hp > 0 and defender_soldier_remaining_hp > 0: #当排头士兵血量不为0且有士兵时
    if hudun_remaining_hp > 0: #护盾值不为0，把护盾加到排头士兵上
        first_soldier_hp_hudun = first_soldier_hp + hudun_remaining_hp
    else:
        first_soldier_hp_hudun = first_soldier_hp

# 输出残血士兵信息（用于调试）
st.write(f"士兵承伤阶段3 - 第二次兵打兵-排头士兵血量: {first_soldier_hp}")

remaining_soldier_to_soldier_segments_used = 0 #用一个变量从0开始记录3阶段的第二次士兵兵打兵段数

# 处理排头士兵
if first_soldier_hp > 0 and defender_soldier_remaining_hp > 0: #当排头士兵血量不为0且有士兵时
    segments_needed_to_kill_last_soldier = math.ceil(first_soldier_hp_hudun / soldier_to_soldier_damage) #计算杀死排头士兵需要多少段兵打兵的段数
    if remaining_soldier_segments >= segments_needed_to_kill_last_soldier: #remaining_soldier_segments是后于英雄出手的士兵段数，若能杀死排头士兵
        # 杀死排头士兵
        remaining_soldier_segments -= segments_needed_to_kill_last_soldier #计算杀死排头士兵后，剩余的兵打兵段数
        defender_soldier_remaining_hp -= first_soldier_hp #计算杀死排头士兵后，当前士兵总血量剩多少
        remaining_soldier_to_soldier_segments_used += segments_needed_to_kill_last_soldier #累计记录第二次兵打兵消耗的段数
        first_soldier_hp = 0 #将排头士兵血量定为0
        soldier_killed_by_soldier += 1  #记录累计士兵杀死士兵的个数
        hudun_remaining_hp = 0  # 剩余护盾值为0
    else:
        # 排头士兵未被打死
        defender_soldier_remaining_hp = min(defender_soldier_remaining_hp,defender_soldier_remaining_hp + hudun_remaining_hp - remaining_soldier_segments * soldier_to_soldier_damage) #当前士兵总血量剩多少
        first_soldier_hp = min(first_soldier_hp , first_soldier_hp_hudun - remaining_soldier_segments * soldier_to_soldier_damage)   #当前排头士兵剩多少
        remaining_soldier_to_soldier_segments_used += remaining_soldier_segments #累计记录第二次兵打兵消耗的段数，没打死就全记录
        hudun_remaining_hp = max(0 , hudun_remaining_hp - remaining_soldier_segments * soldier_to_soldier_damage) # 计算剩余护盾值
        remaining_soldier_segments = 0 #第二次士兵出手的段数消耗完了

#这个阶段完成后，护盾有可能全部消耗，有可能剩余

# 处理满血士兵
for _ in range(defender_soldier_count - 1): #忽略已处理的排头士兵
    if remaining_soldier_segments == 0 or defender_soldier_remaining_hp <= 0: #士兵二阶段段数用完或当前士兵总血量为0即没有士兵了，跳出循环
        break
    current_soldier_hp = defender_soldier_max_hp_per_unit #current_soldier_hp是每只满血士兵血量，等于每只守方士兵最大血量defender_soldier_max_hp_per_unit
    segments_needed_to_kill_soldier = math.ceil(current_soldier_hp / soldier_to_soldier_damage) #计算一只满血的士兵要消耗兵雄打兵多少段

    if remaining_soldier_segments >= segments_needed_to_kill_soldier: #如果士兵二阶段段数足够杀死一只满血士兵
        remaining_soldier_segments -= segments_needed_to_kill_soldier  #计算杀死这只士兵后，士兵二阶段剩余的段数
        defender_soldier_remaining_hp -= current_soldier_hp #计算杀死这只士兵后，当前士兵总血量剩多少
        remaining_soldier_to_soldier_segments_used += segments_needed_to_kill_soldier #累计记录第二次兵打兵消耗的段数
        soldier_killed_by_soldier += 1 #记录累计士兵杀死士兵的个数
    else:
        defender_soldier_remaining_hp -= remaining_soldier_segments * soldier_to_soldier_damage #当前士兵总血量剩多少
        remaining_soldier_to_soldier_segments_used += remaining_soldier_segments #累计记录第二次兵打兵消耗的段数，没打死就全记录
        remaining_soldier_segments = 0 #第二次士兵出手的段数消耗完了
        break

# ------------------------------
# 处理士兵打英雄的段数，加入鞭尸机制
# ------------------------------

# 初始化鞭尸丢失段数
soldier_to_hero_lost_segments_3 = 0 #用一个变更记录鞭尸丢失的段数
soldier_to_hero_segments_used_3 = 0 #士兵打英雄的实际作用段数（未丢失）第3阶段

if not shield_used and defender_soldier_remaining_hp <= 0: #如果护盾没被使用且没有士兵
    if hudun_remaining_hp > 0:
        defender_hero_remaining_hp_hudun = hudun_remaining_hp + defender_hero_remaining_hp
    else:
        defender_hero_remaining_hp_hudun =  defender_hero_remaining_hp

if  remaining_soldier_segments > 0 :
    remaining_soldier_to_hero_segments = remaining_soldier_segments
    # 计算守方英雄剩余血量
    if defender_hero_remaining_hp > 0 and defender_soldier_remaining_hp <= 0: #如果守方英雄剩余血量大于0且没有士兵了
        segments_needed_to_kill_hero = math.ceil(defender_hero_remaining_hp_hudun / soldier_to_hero_damage) #计算守方英雄的剩余血量需要多少段兵打英雄能杀掉
        if remaining_soldier_to_hero_segments >= segments_needed_to_kill_hero: #如果二阶段兵打英雄的段数能杀死英雄
            # 杀死英雄，剩余的段数被鞭尸丢失
            soldier_to_hero_segments_used_3 = segments_needed_to_kill_hero #定义soldier_to_hero_segments_used为士兵打英雄的真实段数
            soldier_to_hero_lost_segments_3 = remaining_soldier_to_hero_segments - segments_needed_to_kill_hero #计算鞭尸丢失的段数
            defender_hero_remaining_hp = 0 #守方英雄剩余血量为0
            if not shield_used:
                hudun_remaining_hp = 0  # 剩余护盾值为0
        else:
            # 英雄未被打死，全部段数都生效
            soldier_to_hero_segments_used_3 = remaining_soldier_to_hero_segments #定义soldier_to_hero_segments_used为士兵打英雄的真实段数，英雄未死全部都算
            soldier_to_hero_lost_segments_3 = 0 #计算鞭尸丢失的段数为0
            defender_hero_remaining_hp = min(defender_hero_remaining_hp , defender_hero_remaining_hp_hudun - remaining_soldier_to_hero_segments * soldier_to_hero_damage) #计算守方英雄的剩余血量
            if not shield_used:
                hudun_remaining_hp = max(0 , hudun_remaining_hp - remaining_soldier_to_hero_segments * soldier_to_hero_damage) # 计算剩余护盾值
    elif defender_hero_remaining_hp <= 0 and defender_soldier_remaining_hp <= 0:     # 如果英雄已经死亡，则所有段数都被鞭尸丢失
        soldier_to_hero_lost_segments_3 = remaining_soldier_to_hero_segments #计算鞭尸丢失的段数全丢了
        soldier_to_hero_segments_used_3 = 0 #士兵打英雄的真实段数为0
else:
    soldier_to_hero_segments_used_3 = 0

soldier_to_hero_segments_used = soldier_to_hero_segments_used_1 + soldier_to_hero_segments_used_3 #计算士兵打英雄实际段数

# ------------------------------
# 计算守方英雄的剩余血量 defender_hero_remaining_hp（前面已计算，不用重复计算）
# ------------------------------

# 分割线
st.divider()

# ------------------------------
# 输出结果
# ------------------------------

# 将2个阶段的士兵打士兵段数合计起来
soldier_to_soldier_segments_used_hj = soldier_to_soldier_segments_used + remaining_soldier_to_soldier_segments_used

# 定义动画丢失段数
bdb_dhds = 0
bdyx_dhds = 0
yxdb_dhds = 0
yxdyx_dhds = 0
dhds_pd = st.checkbox("默认无动画影响的段数丢失，如有请勾选填写动画丢失段数")
# 定义动画丢失段数
if dhds_pd:
    bdb_dhds = round(st.number_input("士兵打士兵的动画丢失段数", min_value=0, value=0))
    bdyx_dhds = round(st.number_input("士兵打英雄的动画丢失段数", min_value=0, value=0))
    yxdb_dhds = round(st.number_input("英雄打士兵的动画丢失段数", min_value=0, value=0))
    yxdyx_dhds = round(st.number_input("英雄打英雄的动画丢失段数", min_value=0, value=0))

# 根据动画丢失段数影响修正段数
soldier_to_soldier_segments_used_hj -= bdb_dhds
soldier_to_hero_segments_used -= bdyx_dhds
hero_to_soldier_segments_used -= yxdb_dhds
hero_to_hero_segments -= yxdyx_dhds

# 输出战斗段数信息
column91, column92, column93 = st.columns([1,0.1,1])
with column91:
    st.write(f"士兵打士兵的段数: {soldier_to_soldier_segments_used_hj} ")
    st.write(f"士兵打英雄的段数: {soldier_to_hero_segments_used} ")
    st.write(f"英雄打士兵的段数: {hero_to_soldier_segments_used} ")
    st.write(f"英雄打英雄的段数: {hero_to_hero_segments} ")
with column93:
    st.write(f"士兵打士兵伤害: {soldier_to_soldier_segments_used_hj * soldier_to_soldier_damage}")
    st.write(f"士兵打英雄伤害: {soldier_to_hero_segments_used * soldier_to_hero_damage}")
    st.write(f"英雄打士兵伤害:{hero_to_soldier_segments_used * hero_to_soldier_damage}")
    st.write(f"英雄打英雄伤害: {hero_to_hero_segments * hero_to_hero_damage}")

# 定义本次单点总伤害
dd_zsh = (soldier_to_soldier_segments_used_hj* soldier_to_soldier_damage + soldier_to_hero_segments_used * soldier_to_hero_damage + hero_to_soldier_segments_used * hero_to_soldier_damage + hero_to_hero_segments * hero_to_hero_damage)
dd_dsb_sh = soldier_to_soldier_segments_used_hj * soldier_to_soldier_damage + hero_to_soldier_segments_used * hero_to_soldier_damage
dd_dyx_sh = soldier_to_hero_segments_used * soldier_to_hero_damage + hero_to_hero_segments * hero_to_hero_damage

# 分割线
st.divider()

# 输出士兵和英雄杀死的士兵数量
st.write(f"士兵杀死士兵数量: {soldier_killed_by_soldier}")
st.write(f"英雄杀死士兵数量: {soldier_killed_by_hero}")

# 分割线
st.divider()

# 输出守方士兵和英雄的剩余血量
st.markdown(f"###### 守方剩余护盾 <strong><span style='color:orange;font-size:20px;'>{hudun_remaining_hp}</span></strong>", unsafe_allow_html=True)
st.markdown(f"##### 守方士兵剩余血量 <strong><span style='color:red;font-size:25px;'>{defender_soldier_remaining_hp}/{defender_soldier_hp}</span></strong>", unsafe_allow_html=True)
st.markdown(f"##### 守方英雄剩余血量 <strong><span style='color:green;font-size:25px;'>{defender_hero_remaining_hp}/{defender_hero_hp}</span></strong>", unsafe_allow_html=True)

# 分割线
st.divider()

st.markdown(f"##### 本次单点总伤害 <strong><span style='color:blue;font-size:25px;'>{dd_zsh}</span></strong>", unsafe_allow_html=True)

st.markdown(f"###### 其中：对士兵造成伤害 <strong><span style='color:gray;font-size:20px;'>{dd_dsb_sh}</span></strong>", unsafe_allow_html=True)
st.markdown(f"###### 其中：对英雄造成伤害 <strong><span style='color:gray;font-size:20px;'>{dd_dyx_sh}</span></strong>", unsafe_allow_html=True)

# 分割线
st.divider()

st.write("目前计算器仍在测试中，aoe计算器开发中，梦战计算器使用交流群 928411216")