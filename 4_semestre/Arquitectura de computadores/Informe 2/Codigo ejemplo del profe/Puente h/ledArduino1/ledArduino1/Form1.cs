using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
//agregar estas lineas para trabajar con el puerto serie
using System.IO.Ports;
using ledArduino.Properties;


namespace ledArduino
{
    public partial class Form1 : Form
    {
        //abre y declara el puerto
        public Form1()
        {
            InitializeComponent();
            serialPort1.PortName = "COM4";
            serialPort1.BaudRate = 9600;
            serialPort1.Open();
        }
        //Cierra el puerto cuando se cierra el form
        private void Form1_ForeClosing(object sender, FormClosedEventArgs e)
        {
            if (serialPort1.IsOpen) serialPort1.Close();
        
        }
        // ----------------------------------------------Lado izquierdo-----------------------------------------------
        private void label3_Click(object sender, EventArgs e)
        {
            // texto sentido 1
        }
        private void on_Click(object sender, EventArgs e)
        {
            // boton ON izquierda
            serialPort1.Write("1");
            on.Enabled = false;
            off.Enabled = true;
            pictureBox1.Image = Resources.on;
            button1.Text = Convert.ToString(5 - (hScrollBar1.Value * 0.05));
            

        }
        private void off_Click(object sender, EventArgs e)
        {
            // boton OFF izquierda
            serialPort1.Write("0");
            on.Enabled = true;
            off.Enabled = false;
            pictureBox1.Image = Resources.off;
            button1.Text = "0";

        }
        private void pictureBox1_Click(object sender, EventArgs e)
        {
            // ampolleta izquierda
        }
        private void label6_Click(object sender, EventArgs e)
        {
            // texto variacion de velocidad izquierda
        }
        private void hScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            // barra horizontal izquierda
            if (on.Enabled == false)
            {
                button1.Text = Convert.ToString(5 - (hScrollBar1.Value * 0.05));
            }
     
        }
        private void label1_Click_1(object sender, EventArgs e)
        {
            // texto velocidad izquierdo
        }
        private void button1_Click(object sender, EventArgs e)
        {
            // boton para proyectar velocidad izquierda
        }
        // ----------------------------------------------Lado derecho-----------------------------------------------
        private void label4_Click(object sender, EventArgs e)
        {
            // texto sentido 2
        }
        private void ON2_Click(object sender, EventArgs e)
        {
            // Boton ON derecha
            serialPort1.Write("3");
            ON2.Enabled = false;
            OFF2.Enabled = true;
            pictureBox2.Image = Resources.on;
            button2.Text = Convert.ToString(5 - (hScrollBar2.Value * 0.05)); ;
        }
        private void OFF2_Click(object sender, EventArgs e)
        {
            //boton OFF derecha
            // Analogwrite(a,b)
            // delay()
            serialPort1.Write("4");
            ON2.Enabled = true;
            OFF2.Enabled = false;
            pictureBox2.Image = Resources.off;
            button2.Text = "0";
        }
        private void pictureBox2_Click(object sender, EventArgs e)
        {
            // ampolleta derecha
        }
        private void label7_Click(object sender, EventArgs e)
        {
            // texto variacion de velocidad derecha
        }
        private void hScrollBar2_Scroll(object sender, ScrollEventArgs e)
        {
            // barra horizontal derecha
            if (OFF2.Enabled == true)
            {
                button2.Text = Convert.ToString(5 - (hScrollBar2.Value * 0.05));
            }
            //button2.Text = Convert.ToString(5 - (hScrollBar2.Value * 0.05));

        }
        private void label2_Click(object sender, EventArgs e)
        {
            // texto  velocidad derecha
        }
        private void button2_Click(object sender, EventArgs e)
        {
            // Boton para proyectar velocidad derecha

        }
        // ----------------- NI PUTA IDEA -------------------------------------
        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }
        // -------------------------------------------------------------------------------------------------------------------------------------
        private void button3_Click(object sender, EventArgs e)
        {
            // 3
            button3.Enabled = false;
            button4.Enabled = true;
            
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // 4
            button4.Enabled = false;
            button3.Enabled = true;
        }
    }
}
