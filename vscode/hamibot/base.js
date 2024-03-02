auto.waitFor();

//获取手机分辨率
var x = device.width;//手机的屏幕宽
var y = device.height;　
//排除某些机型的x、y互换的情况
var i = 0;
if(x>2000)
{
  i = x;
  x = y;
  y = i;
}

// 输入密码
function password_input()
{
    var password = "960924"
    for(var i = 0; i < password.length; i++)
    {
        var p = text(password[i].toString()).findOne().bounds();
        click(p.centerX(), p.centerY());
        sleep(100);
    }
}
 
if(!device.isScreenOn())
    {
        device.wakeUp();
        sleep(1000);
        swipe(x/2,y*0.9,x/2,100,230);
        password_input();
    }