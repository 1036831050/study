auto.waitFor();

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