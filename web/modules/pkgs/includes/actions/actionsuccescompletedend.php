<div class="header">
    <h1>End Success</h1>
</div>

<div class="content">
    <div>
        <input type="hidden" name="step" />
        <input type="hidden" name="actionlabel" value="<?php echo (isset($_POST['actionlabel']))? $_POST['actionlabel'] : uniqid(); ?>"/>
        <input type="hidden" name="action" value="actionsuccescompletedend" />
        <?php
        if(isset($_POST['clear']))
        {
            echo '<p><input type="checkbox" checked onclick="if(jQuery(this).is(\':checked\')){jQuery(this).next().prop(\'disabled\',false);}else{jQuery(this).next().prop(\'disabled\',true);}" />Clear <select name="clear"><option value="True">True</option><option value="False">False</option><select></p>';
        }
        else{
            echo '<p><input type="checkbox" onclick="if(jQuery(this).is(\':checked\')){jQuery(this).next().prop(\'disabled\',false);}else{jQuery(this).next().prop(\'disabled\',true);}" />Clear <select name="clear" disabled><option value="True">True</option><option value="False">False</option><select></p>';
        }?>
    </div>

</div>