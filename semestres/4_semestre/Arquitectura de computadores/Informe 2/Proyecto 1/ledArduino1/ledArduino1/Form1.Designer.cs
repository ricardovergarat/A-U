namespace ledArduino
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador requerida.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén utilizando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben eliminar; false en caso contrario, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido del método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.on = new System.Windows.Forms.Button();
            this.off = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.serialPort1 = new System.IO.Ports.SerialPort(this.components);
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.OFF2 = new System.Windows.Forms.Button();
            this.ON2 = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.hScrollBar1 = new System.Windows.Forms.HScrollBar();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.hScrollBar2 = new System.Windows.Forms.HScrollBar();
            this.button3 = new System.Windows.Forms.Button();
            this.button4 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.SuspendLayout();
            // 
            // on
            // 
            this.on.Location = new System.Drawing.Point(204, 87);
            this.on.Name = "on";
            this.on.Size = new System.Drawing.Size(75, 23);
            this.on.TabIndex = 0;
            this.on.Text = "ON";
            this.on.UseVisualStyleBackColor = true;
            this.on.Click += new System.EventHandler(this.on_Click);
            // 
            // off
            // 
            this.off.Enabled = false;
            this.off.Location = new System.Drawing.Point(307, 87);
            this.off.Name = "off";
            this.off.Size = new System.Drawing.Size(75, 23);
            this.off.TabIndex = 1;
            this.off.Text = "OFF";
            this.off.UseVisualStyleBackColor = true;
            this.off.Click += new System.EventHandler(this.off_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = global::ledArduino.Properties.Resources.off;
            this.pictureBox1.Location = new System.Drawing.Point(266, 136);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(55, 64);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 4;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Click += new System.EventHandler(this.pictureBox1_Click);
            // 
            // pictureBox2
            // 
            this.pictureBox2.Image = global::ledArduino.Properties.Resources.off;
            this.pictureBox2.Location = new System.Drawing.Point(686, 136);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(60, 64);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox2.TabIndex = 8;
            this.pictureBox2.TabStop = false;
            this.pictureBox2.Click += new System.EventHandler(this.pictureBox2_Click);
            // 
            // OFF2
            // 
            this.OFF2.Enabled = false;
            this.OFF2.Location = new System.Drawing.Point(735, 87);
            this.OFF2.Name = "OFF2";
            this.OFF2.Size = new System.Drawing.Size(75, 23);
            this.OFF2.TabIndex = 6;
            this.OFF2.Text = "OFF";
            this.OFF2.UseVisualStyleBackColor = true;
            this.OFF2.Click += new System.EventHandler(this.OFF2_Click);
            // 
            // ON2
            // 
            this.ON2.Location = new System.Drawing.Point(615, 87);
            this.ON2.Name = "ON2";
            this.ON2.Size = new System.Drawing.Size(75, 23);
            this.ON2.TabIndex = 5;
            this.ON2.Text = "ON";
            this.ON2.UseVisualStyleBackColor = true;
            this.ON2.Click += new System.EventHandler(this.ON2_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(440, 596);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(66, 13);
            this.label5.TabIndex = 15;
            this.label5.Text = "@FTR 2019";
            this.label5.Click += new System.EventHandler(this.label5_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(263, 334);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(54, 13);
            this.label1.TabIndex = 18;
            this.label1.Text = "Velocidad";
            this.label1.Click += new System.EventHandler(this.label1_Click_1);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(692, 334);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(54, 13);
            this.label2.TabIndex = 19;
            this.label2.Text = "Velocidad";
            this.label2.Click += new System.EventHandler(this.label2_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(277, 35);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(52, 13);
            this.label3.TabIndex = 20;
            this.label3.Text = "Sentido 1";
            this.label3.Click += new System.EventHandler(this.label3_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(695, 34);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(52, 13);
            this.label4.TabIndex = 21;
            this.label4.Text = "Sentido 2";
            this.label4.Click += new System.EventHandler(this.label4_Click);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(214, 378);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(142, 70);
            this.button1.TabIndex = 22;
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(658, 378);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(131, 70);
            this.button2.TabIndex = 23;
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // hScrollBar1
            // 
            this.hScrollBar1.Location = new System.Drawing.Point(249, 277);
            this.hScrollBar1.Maximum = 109;
            this.hScrollBar1.Name = "hScrollBar1";
            this.hScrollBar1.Size = new System.Drawing.Size(80, 17);
            this.hScrollBar1.TabIndex = 24;
            this.hScrollBar1.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hScrollBar1_Scroll);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(241, 237);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(115, 13);
            this.label6.TabIndex = 25;
            this.label6.Text = "Variacion de velocidad";
            this.label6.Click += new System.EventHandler(this.label6_Click);
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(655, 237);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(115, 13);
            this.label7.TabIndex = 40;
            this.label7.Text = "Variacion de velocidad";
            this.label7.Click += new System.EventHandler(this.label7_Click);
            // 
            // hScrollBar2
            // 
            this.hScrollBar2.Location = new System.Drawing.Point(676, 277);
            this.hScrollBar2.Maximum = 109;
            this.hScrollBar2.Name = "hScrollBar2";
            this.hScrollBar2.Size = new System.Drawing.Size(80, 17);
            this.hScrollBar2.TabIndex = 27;
            this.hScrollBar2.Scroll += new System.Windows.Forms.ScrollEventHandler(this.hScrollBar2_Scroll);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(389, 493);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 41;
            this.button3.Text = "button3";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // button4
            // 
            this.button4.Enabled = false;
            this.button4.Location = new System.Drawing.Point(519, 493);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(75, 23);
            this.button4.TabIndex = 42;
            this.button4.Text = "button4";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1033, 653);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.hScrollBar2);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.hScrollBar1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.OFF2);
            this.Controls.Add(this.ON2);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.off);
            this.Controls.Add(this.on);
            this.Name = "Form1";
            this.Text = "Modelo Control Domótico";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button on;
        private System.Windows.Forms.Button off;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.IO.Ports.SerialPort serialPort1;
        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.Button OFF2;
        private System.Windows.Forms.Button ON2;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.HScrollBar hScrollBar1;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.HScrollBar hScrollBar2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.Button button4;
    }
}

