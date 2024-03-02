/*
 * @作者: lmd
 * @Date: 2023-02-04 21:45:47
 * @最近编辑人: 梁明东
 * @LastEditTime: 2023-02-06 12:49:21
 * Copyright: 2023 xxxTech CO.,LTD. All Rights Reserved.
 */
auto.waitFor();
/*等待时间*/
function wait_1s(len)
{
    for (let i = 0;i<len;i++){
    sleep(1000)
    toast(i+1)
    }  
}
function wait_1m(len){
    for (let i = 0;i<len;i++){
    wait_1s(60)
    }
}

/*定义上滑动作*/
function upslid()
{
    device.wakeUp();
    sleep(500);
    swipe(500,2000,500,200,201);
}
/*定义解锁手机*/
function unlock(msg)
{
    upslid();
    password_input(msg)
}
/*输入解锁密码*/
function password_input(msg)
{
    var password = msg
    for(var i = 0; i < password.length; i++)
    {
        var p = text(password[i].toString()).findOne().bounds();
        click(p.centerX(), p.centerY());
        sleep(100);
    }
}
///音量调节
function voliceSet()
{
    bat=device.getMusicVolume()
    if (bat != 0){device.setMusicVolume(0)};
}


function beswipe(ti,count)
{
    console.show();
    for (i = 1; i <= count; i++)
    {
    console.log('第%d次',i);
    voliceSet()
    swipe(500,2000,500,200,201);
    tis = getrandom(ti)
    toastLog(tis)
    sleep(2*1000)
    if (tis <= ti)
    {
        console.log("点赞");
        try
        {
            id("like_count_view").className("android.widget.TextView").findOne().parent().click()
        }
        catch(err)
        {
            //pass
        }
    }
    sleep((tis-2)*1000)
    }
    console.hide();
}
///获取随机数
function getrandom(max)
{
    ///min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * max + 5 );
}

//点赞
// function doubleClick()
// {
//     className("android.widget.TextView").clickable(false).findOne().click()
//     //click(995,1227)
// }
///if(!device.isScreenOn()){device.wakeUp()}
function main(passwd,counts)
{
    if (device.isScreenOn()){
        //pass
    }
    else {device.wakeUp();
    unlock(passwd)}
    var pacname = getPackageName('抖音极速版')
    launch(pacname)
    sleep(4)
    beswipe(15,counts)
}
///className("android.widget.FrameLayout").clickable(true).findOne().click()   点击继续看视频赚钱
//id("like_count_view").className("android.widget.TextView").findOne().parent().click()
///脚本开始执行区域
main("960924",1000);
