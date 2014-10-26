using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;
using DeviceSDK;
using DeviceSDK.Miscellaneous;

namespace 宠物信息录入查询系统
{
    public partial class form1 : Form
    {
        PTDevice _oDevice;
        private bool USBConnect(String sPort)
        {
            if (_oDevice != null)
            {
                _oDevice.Close();
                _oDevice = null;
            }

            try
            {
                PTDevice oDevice = new PTDevice(sPort, null);
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
        public form1()
        {
            int count = 2;
            while (count < 1000)
            {

                if (USBConnect(count.ToString()) == true)
                {
                    break;
                }
                count++;
            }
            if (count >= 1000)
            {
                MessageBox.Show("未检测到对端设备,点击确定退出程序");
                //Environment.Exit(0);
            }

            InitializeComponent();
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
