import tkinter as tk    #tkinterライブラリを呼び出してエイリアスで別名をつける
from tkinter import ttk, messagebox #fromはPythonのtkinterライブラリからttkとmessageboxという2つのモジュール（サブモジュール）をインポートすることを意味します。
"""
ttk
ttkはtkinterの一部で、「themed tkinter widgets（テーマ付きのウィジェット）」の略です。
目的: ttkモジュールは、よりモダンでカスタマイズ可能なウィジェット（例えば、ボタン、ラベル、エントリフィールドなど）を提供します。従来のtkinterウィジェットよりもスタイリッシュで、デフォルトの見た目が改善されています。
messagebox
messageboxもtkinterの一部で、ユーザーにメッセージを表示するためのポップアップウィンドウ（ダイアログボックス）を作成するために使います。
目的: messageboxを使うことで、情報、警告、エラーメッセージなどを簡単にユーザーに提示することができます。
"""
import cv2
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image, ImageTk
"""
cv2 の概要
OpenCVは、もともとインテルによって開発されたオープンソースのライブラリで、画像処理、コンピュータビジョン、機械学習のさまざまなタスクを効率的に実行するための機能を提供しています。
**cv2**はOpenCVのPythonインターフェースです。C++で書かれたOpenCVの関数をPythonから利用できるようにしたものです。
cv2 の主な機能
画像の読み込み、表示、保存:
cv2.imread()を使って画像を読み込み、cv2.imshow()で表示し、cv2.imwrite()で保存します。
ビデオのキャプチャと処理:
ウェブカメラやビデオファイルからビデオをキャプチャすることができます。cv2.VideoCapture()を使用してキャプチャし、フレームごとに処理を行います。
画像の変換:
画像のリサイズ、回転、切り抜き、色変換（例: RGBからグレースケール）など、さまざまな画像変換を行うことができます。
画像のフィルタリング:
ぼかし、シャープネス、エッジ検出などの画像フィルタリングを行うことができます。cv2.filter2D()やcv2.Canny()などの関数を使用します。
特徴量検出とマッチング:
SIFT、SURF、ORBなどのアルゴリズムを使って画像の特徴量を検出し、それらをマッチングすることができます。
機械学習とディープラーニング:
OpenCVには、画像分類、オブジェクト検出、セグメンテーションなどのための機械学習およびディープラーニングのモデルが多数組み込まれています。
幾何変換と画像の歪み補正:
画像の視点変換や歪み補正などの幾何学的な変換を行うことができます。
"""

import pymssql
import os
"""
import os の意味
import os は、Pythonの標準ライブラリであるosモジュールをインポートするコードです。このモジュールを使うことで、オペレーティングシステム（OS）に依存する機能をPythonプログラムで利用できるようになります。具体的には、ファイルやディレクトリの操作、環境変数の取得や設定、プロセスの管理などが含まれます。

os モジュールの主な機能
osモジュールには、さまざまなOS操作をサポートする関数が多数含まれています。以下に主な機能とその例を紹介します。

ファイルとディレクトリの操作

os.listdir(path): 指定したディレクトリの中にあるファイルやディレクトリのリストを返します。
os.mkdir(path): 新しいディレクトリを作成します。
os.makedirs(path): 必要に応じて親ディレクトリも含めてディレクトリを再帰的に作成します。
os.remove(path): 指定したファイルを削除します。
os.rmdir(path): 指定したディレクトリを削除します（ディレクトリが空である必要があります）。
os.rename(src, dst): ファイルまたはディレクトリの名前を変更します。
環境変数の操作

os.environ: 環境変数を取得または設定するためのマッピングオブジェクトです。
os.getenv(key, default=None): 指定した環境変数の値を取得します。存在しない場合はデフォルト値を返します。
os.putenv(key, value): 環境変数を設定します。
現在の作業ディレクトリの取得と変更

os.getcwd(): 現在の作業ディレクトリ（カレントディレクトリ）を取得します。
os.chdir(path): 作業ディレクトリを変更します。
パス操作

os.path: ファイルパスの操作を行うためのサブモジュールです。例えば、os.path.join()やos.path.exists()などの関数があります。
システム情報

os.name: 使用しているOSの名前を返します（例: 'posix'、'nt'）。
os.system(command): シェルでコマンドを実行します。
"""

class BarcodeApp:
    """
    クラス（Class）:
        クラスは、オブジェクトの設計図やテンプレートのようなものです。特定の種類のオブジェクトが持つべき属性やメソッドを定義します。
        クラスそのものはオブジェクトではなく、そのクラスをもとにして作られる具体的なインスタンス（オブジェクト）が実際に使われます。

    インスタンス（Instance）:
        インスタンスは、クラスから作成される具体的なオブジェクトです。インスタンスはクラスの定義に従って属性とメソッドを持ちます。
        例えば、Personというクラスがある場合、「John」というインスタンスを作成できます。このインスタンスはPersonクラスに定義された属性（例えば名前や年齢）とメソッド（例えば話す、歩く）を持ちます。

    属性（Attributes）:
        属性は、クラスで定義される変数です。オブジェクトの状態やデータを保持します。    
        例：name、age、heightなど。

    メソッド（Methods）:
        メソッドは、クラスで定義される関数です。オブジェクトの動作や機能を定義します。
        例：speak()、walk()、get_age()など。
     """
    
            
    def __init__(self, root):   #イニシャライザー クラスが作成されたとき１回だけ実行される。※インスタンス（オブジェクト）を初期化する
        self.root = root    # メインウィンドウオブジェクトをインスタンス変数self.rootに保存
        """
        self の意味
         selfは、Pythonクラスの中でインスタンス自身を参照するためのキーワードです。クラスのメソッドを定義するとき、メソッドの最初の引数としてselfを使うのが慣例です。このselfを通じて、そのクラスのインスタンス変数（属性）やメソッドにアクセスすることができます。
        root の意味
            rootは、通常、tkinterを使用しているときに「ルートウィンドウ」を指すために使われる変数名です。tkinterはPythonの標準GUIライブラリであり、rootという変数名は通常tk.Tk()のインスタンスを表します。tk.Tk()は、tkinterで最初に作成されるメインウィンドウのオブジェクトです。
        self.root の意味
            self.rootは、クラス内でrootという名前のインスタンス属性を定義し、その属性がtk.Tk()のインスタンスを指していることを意味します。これは、そのクラスがtkinterを使ったGUIアプリケーションのクラスであることを示唆しています。
        """

        self.root.title("Barcode Reader")   # ウィンドウタイトルを設定
        
        # メインフレームの設定
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)  # フレームにパディングを追加して、余白を設定

        # ラベルとエントリフィールドの設定
        self.label = ttk.Label(self.frame, text="品目CD:")
        self.label.grid(row=0, column=0, padx=(0, 0), pady=(0, 10), sticky='w')

        self.code_entry = ttk.Entry(self.frame, width=30)
        self.code_entry.grid(row=0, column=1, padx=(0, 0), pady=(0, 10), sticky='w')
        self.code_entry.bind('<Return>', self.check_product_in_db)

        self.add_button = ttk.Button(self.frame, text="追加", command=self.add_to_list)
        self.add_button.grid(row=0, column=2, padx=(0, 5), pady=(0, 10), sticky="e")

        self.quantity_label = ttk.Label(self.frame, text="出庫数量:")
        self.quantity_label.grid(row=1, column=0, padx=(0, 0), pady=(0, 10), sticky='w')

        self.update_button = ttk.Button(self.frame, text="更新", command=self.update_quantity)
        self.update_button.grid(row=1, column=1, padx=(5, 0), pady=(0, 10), sticky="e")

        self.quantity_entry = ttk.Entry(self.frame, width=10)
        self.quantity_entry.grid(row=1, column=1, padx=(0, 0), pady=(0, 10), sticky='w')

        self.delete_button = ttk.Button(self.frame, text="削除", command=self.delete_selected)
        self.delete_button.grid(row=2, column=2, padx=(5, 0), pady=(0, 10), sticky="e")

        # Treeviewウィジェットの作成
        self.list_label = ttk.Label(self.frame, text="登録済:")
        self.list_label.grid(row=3, column=0, columnspan=4, padx=(0, 5), pady=(10, 5), sticky='w')

        self.product_tree = ttk.Treeview(self.frame, columns=("Code", "Name", "Quantity", "ZaikoQuantity"), show="headings", height=8)
        self.product_tree.heading("Code", text="品目CD")
        self.product_tree.heading("Name", text="品名")
        self.product_tree.heading("Quantity", text="出庫数量")
        self.product_tree.heading("ZaikoQuantity", text="在庫数量")
        self.product_tree.column("Code", width=100)
        self.product_tree.column("Name", width=150)
        self.product_tree.column("Quantity", width=10)
        self.product_tree.column("ZaikoQuantity", width=10)
        self.product_tree.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

        # Treeviewの選択イベントをバインド
        self.product_tree.bind('<<TreeviewSelect>>', self.on_tree_select)

        # 送信ボタン
        self.submit_button = ttk.Button(self.frame, text="送信", command=self.submit_data)
        self.submit_button.grid(row=5, column=2, padx=(5, 0), pady=(10, 0), sticky="e")

        # 画像ラベルの設定
        self.image_label = ttk.Label(self.frame)
        self.image_label.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

        self.camera_label = ttk.Label(self.frame)
        self.camera_label.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

        # カメラの初期化と映像の更新
        self.cap = cv2.VideoCapture(0)
        self.update_image()

        self.products = {}
        
    def update_image(self):
        ret, frame = self.cap.read()    #カメラから映像を取得する
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.camera_label.imgtk = imgtk
            self.camera_label.configure(image=imgtk)

            decoded_objects = decode(frame, symbols=[ZBarSymbol.QRCODE, ZBarSymbol.EAN13, ZBarSymbol.CODE128, ZBarSymbol.CODE39])
            for obj in decoded_objects:
                try:
                    barcode_data = obj.data.decode('utf-8')
                    self.code_entry.delete(0, tk.END)
                    self.code_entry.insert(0, barcode_data)
                    self.check_product_in_db()
                    # self.display_product_image(barcode_data)    画像表示をしようするのであれば
                except Exception as e:
                    print(f"Error バーコードを読み取れません。: {e}")
                break

        self.root.after(100, self.update_image)
    """
    def display_product_image(self, product_code):
        #Display the image corresponding to the product code.
        image_path = f"{product_code}.jpg"  # Assuming images are named as product_code.jpg
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((200, 200))  # Resize the image if needed
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference to avoid garbage collection
        else:
            self.image_label.config(image='')
    
    def show_selected_image(self, event):
        #Display the image of the selected product in the listbox.
        selected_index = self.product_listbox.curselection()
        if selected_index:
            selected_text = self.product_listbox.get(selected_index)
            product_code = selected_text.split(",")[0].split(":")[1].strip()
            self.display_product_image(product_code)
    """
    def check_product_in_db(self, event=None):
        """Check if the product code exists in the database and set the quantity if it does."""
        product_code = self.code_entry.get()
        if product_code:
            try:
                conn = pymssql.connect(server='10.177.1.103', user='coresysuser', password='tsurudb@1234567890', database='as400')
                cursor = conn.cursor()
                cursor.execute("SELECT ITNAM1,ITMRYO FROM as400.dbo.AS_T_M_ITEM WHERE ITHBAN = %s", (product_code,))
                result = cursor.fetchone()
                if result:
                    self.quantity_entry.delete(0, tk.END)
                    self.quantity_entry.insert(0, result[0])
                cursor.close()
                conn.close()
            except Exception as e:
                messagebox.showerror("Database Error", f"Failed to check product in database: {e}")

    def add_to_list(self):
        # 入力フィールドから値を取得
        product_code = self.code_entry.get()
        quantity = self.quantity_entry.get()

        # 値がすべて入力されている場合にTreeviewに追加
        if product_code and quantity:
            # Check if the product exists in the database and if the quantity is sufficient
            try:
                # データベースに接続
                conn = pymssql.connect(server='10.177.1.103', user='coresysuser', password='tsurudb@1234567890', database='as400')
                cursor = conn.cursor()
                
                # SQLクエリを実行して結果を取得
                cursor.execute("SELECT ITNAM1,ITMRYO FROM as400.dbo.AS_T_M_ITEM WHERE ITHNBN = %s", (product_code,))
                result = cursor.fetchone()

                # 品目がデータベースに存在しない場合
                if not result:
                    messagebox.showerror("Product Error", "品目CDがデータに登録されていません。")
                    return
                
                # 品目が存在する場合は数量をチェック
                try:
                    self.product_name = result[0]
                    self.zaiko_quantity = result[1]
                    available_quantity = int(result[1])  # データベースから取得した在庫数量を整数に変換
                except ValueError:
                    messagebox.showerror("Data Error", "データベースから取得した数量が無効です。")
                    return

                if available_quantity < int(quantity):
                    messagebox.showerror("Quantity Error", f"Insufficient quantity in database. Available: {available_quantity}")
                    return

                # データベース接続を閉じる
                cursor.close()
                conn.close()

            except Exception as e:
                messagebox.showerror("Database Error", f"Failed to check product in database: {e}")
                return

            # 同じ品目コードが既にリストに存在する場合の処理
            if product_code in self.products:
                messagebox.showerror("Duplicate Error", "This product code is already in the list.")
                return

            # 正常な場合はリストに追加
            
            self.products[product_code] = quantity
            self.product_tree.insert("", tk.END, values=(product_code, self.product_name, quantity, self.zaiko_quantity))
            self.code_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
            self.code_entry.focus_set()
            #　self.display_product_image(product_code)  画像表示をしようするのであれば

        else:
            messagebox.showwarning("Input Error", "Please enter both product code and quantity.")
    """       
    def add_to_list(self):
        product_code = self.code_entry.get()
        quantity = self.quantity_entry.get()

        if product_code and quantity:
            # Check if the product exists in the database and if the quantity is sufficient
            try:
                conn = pymssql.connect(server='server_name', user='user', password='password', database='database_name')
                cursor = conn.cursor()
                cursor.execute("SELECT Quantity FROM Products WHERE ProductCode = %s", (product_code,))
                result = cursor.fetchone()
                if not result:
                    messagebox.showerror("Product Error", "This product code does not exist in the database.")
                    return
                elif int(result[0]) < int(quantity):
                    messagebox.showerror("Quantity Error", f"Insufficient quantity in database. Available: {result[0]}")
                    return
                cursor.close()
                conn.close()
            except Exception as e:
                messagebox.showerror("Database Error", f"Failed to check product in database: {e}")
                return

            if product_code in self.products:
                messagebox.showerror("Duplicate Error", "This product code is already in the list.")
                return
            
            self.products[product_code] = quantity
            self.product_listbox.insert(tk.END, f"Code: {product_code}, Quantity: {quantity}")
            self.code_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
            self.code_entry.focus_set()
            self.display_product_image(product_code)  # Display image after adding to list
        else:
            messagebox.showwarning("Input Error", "Please enter both product code and quantity.")
    """
    def update_quantity(self):
        try:
            selected_item = self.product_tree.selection()[0]
            item_values = self.product_tree.item(selected_item, 'values')
            product_code = item_values[0]
            new_quantity = self.quantity_entry.get()

            if not new_quantity:
                messagebox.showwarning("Input Error", "新しい数量を入力してください。")
                return

            try:
                conn = pymssql.connect(server='10.177.1.103', user='coresysuser', password='tsurudb@123456789', database='as400')
                cursor = conn.cursor()
                
                cursor.execute("SELECT ITMRYO FROM as400.dbo.AS_T_M_ITEM WHERE ITHNBN = %s", (product_code,))
                result = cursor.fetchone()

                if result:
                    available_quantity = int(result[0])  # データベースから取得した在庫数量を整数に変換
                    if int(new_quantity) > available_quantity:
                        messagebox.showerror("Quantity Error", f"在庫が不足しています。 利用可能な数量: {available_quantity}")
                        return

                cursor.close()
                conn.close()

            except Exception as e:
                messagebox.showerror("Database Error", f"{product_code}Failed to check product in database: {e}")
                return

            self.product_tree.item(selected_item, values=(product_code, item_values[1], new_quantity))
            self.products[product_code] = new_quantity
            self.quantity_entry.delete(0, tk.END)
        except IndexError:
            messagebox.showwarning("Selection Error", "更新するアイテムを選択してください。")


    def delete_selected(self):
        try:
            # Treeviewで選択されたアイテムのIDを取得
            selected_item = self.product_tree.selection()[0]  # 修正: curselection()からselection()に変更
            # 選択されたアイテムの値を取得
            item_values = self.product_tree.item(selected_item, 'values')
            product_code = item_values[0]  # "品目CD"の取得
            # 製品リストから選択された商品を削除
            del self.products[product_code]
            self.product_tree.delete(selected_item)  # Treeviewから選択されたアイテムを削除
            self.image_label.config(image='')  # アイテム削除後に画像をクリア
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select an item to delete.")

    def on_tree_select(self, event):
        """Treeviewでアイテムが選択されたときに呼び出される。選択されたアイテムのデータを転記する。"""
        try:
            selected_item = self.product_tree.selection()[0]
            item_values = self.product_tree.item(selected_item, 'values')
            product_code = item_values[0]
            quantity = item_values[2]

            # 転記するデータをエントリフィールドに設定
            self.code_entry.delete(0, tk.END)
            self.code_entry.insert(0, product_code)
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, quantity)
        except IndexError:
            pass
       
    def submit_data(self):
        if not self.products:
            messagebox.showwarning("No Products", "No products to submit.")
            return

        try:
            conn = pymssql.connect(server='10.177.1.103', user='coresysuser', password='tsurudb@123456789', database='as400')
            cursor = conn.cursor()
            for product_code, quantity in self.products.items():
                cursor.execute("INSERT INTO Products (ProductCode, Quantity) VALUES (%s, %d)", (product_code, int(quantity)))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Success", "All data submitted successfully!")
            self.product_tree.delete(0, tk.END)
            self.products.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to submit data: {e}")
 
if __name__ == "__main__":
    root = tk.Tk()
    app = BarcodeApp(root)
    root.mainloop()
    
