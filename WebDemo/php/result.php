<?php
    while(1) {
        $file = 'D:\Apache24\htdocs\SolarBurst\images\processed.png';
        if(file_exists($file)){
            echo "图片处理完成";
            echo"<br/>";
            echo'<img src="images/processed.png" alt="图片加载失败">';
            break;
        }
    }


