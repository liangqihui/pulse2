<?php
require_once("../xmlrpc.php");
require_once("../../../../includes/session.inc.php");
require_once("../../../../includes/xmlrpc.inc.php");
extract($_POST);
?>
<div class="header">
    <h1>User Comment</h1>
</div>

<div class="content">
    <div>
        <input type="hidden" name="step" />
        <input type="hidden" name="action" value="action_comment" />
        <?php

        $lab =  (isset($actionlabel))? $actionlabel : uniqid();
        echo'
        <table>
            <tr>
                <th width="16%">Step label : </th>
                <th width="25%">
                    <input type="text" name="actionlabel" value="'.$lab.'"/>
                <th></th>
                <th></th>
            </tr>
            <tr>
             ';
            echo '<td width="16%">
                   User Comment
                </td>
                <td width="25%">
                <textarea name="comment" cols="5" rows="2">';
                echo (isset($comment)) ? $comment : "JID AMR : @@@JID_MASTER@@@[@@@IP_MASTER@@@]
JID ARS : @@@JID_RELAYSERVER@@@[@@@IP_RELAYSERVER@@@]
JID AM  : @@@JID_MACHINE@@@[@@@IP_MACHINE@@@]
Package name : @@@PACKAGE_NAME@@@
Deployement session id : @@@SESSION_ID@@@
Hostname : @@@HOSTNAME@@@
Python implentation : @@@PYTHON_IMPLEMENTATION@@@
Machine architecture : @@@ARCHI_MACHINE@@@
OS family : @@@OS_FAMILY@@@
OS complete name :   @@@OS_COMPLET_NAME@@@
Package UUID : @@@UUID_PACKAGE@@@
Package folder : @@@PACKAGE_DIRECTORY_ABS_MACHINE@@@
List of network interfaces :@@@LIST_INTERFACE_NET@@@
List of MAC addresses : @@@LIST_MAC_ADRESS@@@
list of IP addresses : @@@LIST_IP_ADRESS@@@
Machine IP address connected to XMPP : @@@IP_MACHINE_XMPP@@@
Machine tmp folder : @@@TMP_DIR@@@
" ;
                echo '</textarea>';
                echo'
                </td>';
        echo '
        <td></td><td></td>
            </tr>
        </table>';
        ?>

    </div>

    <input class="btn btn-primary" type="button" onclick="jQuery(this).parent().parent('li').detach()" value="Delete" />
</div>