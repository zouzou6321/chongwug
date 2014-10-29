using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Threading;
using DeviceSDK;
using DeviceSDK.Miscellaneous;

namespace BTDemo {
    public partial class form1 : Form {

        PTDevice _oDevice;
        Thread SecondThread;
        private delegate void Comitjs(String idnum);
        private bool USBConnect(string sport)
        {
            if (_oDevice != null)
            {
                _oDevice.Close();
                _oDevice = null;
            }

            try
            {
                PTDevice oDevice = new PTDevice("USB", null);
                if (!oDevice.Open())
                {
                    return false;
                }

                _oDevice = oDevice;
            }
            catch (Exception err)
            {
                return false;
            }
            return true;
        }

        public form1() {
            InitializeComponent();
            
            if (USBConnect("USB") == false)
            {
                string[] myPortNames = System.IO.Ports.SerialPort.GetPortNames();
                int count = 0;
                foreach (string name in myPortNames)
                {
                    MessageBox.Show(name);
                    if (USBConnect(name) == true)
                    {
                        break;
                    }
                    count++;
                }

                if (count == myPortNames.Length)
                {
                    MessageBox.Show("未检测到对端设备,点击确定退出程序");
                    //Environment.Exit(0);
                }
            }
            webBrowser1.ScriptErrorsSuppressed = true;
        }

        private void FormDemo_FormClosing(object sender, FormClosingEventArgs e) {
            if (_oDevice != null) {
                _oDevice.Close();
                _oDevice = null;
            }
        }

        private string getIdNum(int index)
        {
            PTDevice.Record record = _oDevice.GetRecord(index);
            return record.GetId();
        }

        private void commitWithJs(String idnum) 
        {
            if (webBrowser1.Document != null)
            {
                if (webBrowser1.Document.GetElementById("brogetnum").InnerText == "0")
                {
                    webBrowser1.Document.GetElementById("brosetnum").InnerText = idnum;
                }
            }
        }
        int status = 0;
        private void startDataPro()
        {
            int nCount = 0;
            String idnum = "";
            int i = 0;
            while (true)
            {
                if (_oDevice.IsValid)
                {
                    nCount = _oDevice.GetRecordCount();
                    idnum = "";
                    for (i = 0; i < nCount; i++)
                    {
                        idnum = getIdNum(i);
                    
                        status = 1;
                        while (status != 0)
                        {
                            if (!this.IsDisposed)
                            {
                                this.Invoke((EventHandler)delegate
                                {
                                    if (webBrowser1.Document != null)
                                    {
                                        if (webBrowser1.Document.GetElementById("brogetnum").InnerText == "0")
                                        {
                                            webBrowser1.Document.GetElementById("brosetnum").InnerText = idnum;
                                            status = 0;
                                        }
                                    }
                                });
                            }
                            else
                            {
                                Environment.Exit(0);
                                return;
                            }
                            Thread.Sleep(1000);
                        }
                    }
                    _oDevice.ClearAllRecords(); 
                }
                Thread.Sleep(2000);
            }
        }

        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            if (e.Url.LocalPath == "/petmicro/")
            {
                if (SecondThread == null)
                {
                    SecondThread = new Thread(new ThreadStart(startDataPro));
                    SecondThread.Start();
                }
                
            }
        }
    }
}