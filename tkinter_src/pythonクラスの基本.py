"""
成績表クラス

・生徒の名前
・数学の点数    ・国語の点数    ・英語の点数
・３強化の平均点を計算する

Aさんの成績表  インスタンス（オブジェト）
　堀内A
    １００点    ６０点  ３０点
    ３教科の平均点を計算する

Bさんの成績表  インスタンス（オブジェト）
　小林B
    ９０点    １０点  ２０点
    ３教科の平均点を計算する
"""

class SchoolReport:

    school_name = 'おばか大学'
    def __init__(self,student_name,math_score,jp_score,en_score):
        self.student_name = student_name
        self.math_score = math_score
        self.jp_score = jp_score
        self.en_score = en_score
    
    def calc_avg_score(self):
        sum_score = (self.math_score
                 + self.jp_score
                 + self.en_score)
        avg_score = sum_score /3
        return avg_score
    
sr_a = SchoolReport('堀内A',100,80,70)
avg_a =  sr_a.calc_avg_score()
print(f'Aさんの３教科平均点：{avg_a}')

sr_b = SchoolReport('小林B',99,23,30)
avg_b = sr_b.calc_avg_score()
print(f'Bさんの３教科平均点：{avg_b}') 
