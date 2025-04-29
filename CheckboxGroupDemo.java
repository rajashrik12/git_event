//CheckboxGroup Demo...
import java.awt.*;
import java.awt.event.*;

class CheckboxGroupDemo extends Frame implements ItemListener
{
  Checkbox c1,c2,c3;
  CheckboxGroup cbg;
  Label L1;
  CheckboxGroupDemo()
  {
	FlowLayout f1=new FlowLayout();
	setLayout(f1);
	setBackground(Color.cyan);
	setForeground(Color.black);
	
	cbg=new CheckboxGroup();
	
	c1=new Checkbox("Male",false,cbg);
	c2=new Checkbox("Female",false,cbg);
	c3=new Checkbox("Other",false,cbg);
	L1=new Label("																				");
	add(c1);
	add(c2);
	add(c3);
	add(L1);
	
	c1.addItemListener(this);
	c2.addItemListener(this);
	c3.addItemListener(this);
	
  }
  public void itemStateChanged(ItemEvent ie)
  {
		Checkbox result=cbg.getSelectedCheckbox();
		String str=result.getLabel();
		L1.setText("You have Selected Option:" +str);
  }
  public static void main(String args[])
  {	
	CheckboxGroupDemo f1=new CheckboxGroupDemo();
	f1.setVisible(true);
	f1.setSize(800,800);
	f1.setTitle("Checkbox Group Demo");
  }
}
