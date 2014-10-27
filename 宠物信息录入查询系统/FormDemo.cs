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
                    MessageBox.Show("Open Port Failed!");
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
                    Environment.Exit(0);
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

        private void startDataPro()
        {
            int nCount = _oDevice.GetRecordCount();
            String idnum = "";
            for (int i = 0; i < nCount; i++)
            {
                idnum = getIdNum(i);
                commitWithJs(idnum);
                Thread.Sleep(1000);
            }
        }
        private void commitWithJs(String idnum) 
        {
            Object[] objArray = new Object[1];
            objArray[0] = (Object)idnum;
            if ((webBrowser1.Document != null) && (!idnum.Equals("")))
            {
                if ((int)webBrowser1.Document.InvokeScript("get_idnum") == 0)
                {
                    webBrowser1.Document.InvokeScript("set_idnum", objArray);
                }
            }
        }
        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            if (e.Url.LocalPath == "/petmicro/")
            {
                startDataPro();
            }
        }

    }
}