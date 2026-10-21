# trigger_help()

- **Type:** Function
- **File:** [`modules/trigger/trigger.module`](_file.md), lines 11–37 · [local source](../../../../source/modules/trigger/trigger.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module#L11-L37)
- **Module/theme:** trigger
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function trigger_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function trigger_help($path, $arg) {
  // Generate help text for admin/structure/trigger/(module) tabs.
  $matches = array();
  if (preg_match('|^admin/structure/trigger/(.*)$|', $path, $matches)) {
    $explanation = '<p>' . t('Triggers are events on your site, such as new content being added or a user logging in. The Trigger module associates these triggers with actions (functional tasks), such as unpublishing content containing certain keywords or e-mailing an administrator. The <a href="@url">Actions settings page</a> contains a list of existing actions and provides the ability to create and configure advanced actions (actions requiring configuration, such as an e-mail address or a list of banned words).', array('@url' => url('admin/config/system/actions'))) . '</p>';

    $module = $matches[1];
    $trigger_info = _trigger_tab_information();
    if (!empty($trigger_info[$module])) {
      $explanation .= '<p>' . t('There is a tab on this page for each module that defines triggers. On this tab you can assign actions to run when triggers from the <a href="@module-help">@module-name module</a> happen.', array('@module-help' => url('admin/help/' . $module), '@module-name' => $trigger_info[$module])) . '</p>';
    }

    return $explanation;
  }

  if ($path == 'admin/help#trigger') {
    $output = '';
    $output .= '<h3>' . t('About') . '</h3>';
    $output .= '<p>' . t('The Trigger module provides the ability to cause <em>actions</em> to run when certain <em>triggers</em> take place on your site. Triggers are events, such as new content being added to your site or a user logging in, and actions are tasks, such as unpublishing content or e-mailing an administrator. For more information, see the online handbook entry for <a href="@trigger">Trigger module</a>.', array('@trigger' => 'http://drupal.org/documentation/modules/trigger/')) . '</p>';
    $output .= '<h3>' . t('Uses') . '</h3>';
    $output .= '<dl>';
    $output .= '<dt>' . t('Configuring triggers and actions') . '</dt>';
    $output .= '<dd>' . t('The combination of actions and triggers can perform many useful tasks, such as e-mailing an administrator if a user account is deleted, or automatically unpublishing comments that contain certain words. To set up a trigger/action combination, first visit the <a href="@actions-page">Actions configuration page</a>, where you can either verify that the action you want is already listed, or create a new <em>advanced</em> action. You will need to set up an advanced action if there are configuration options in your trigger/action combination, such as specifying an e-mail address or a list of banned words. After configuring or verifying your action, visit the <a href="@triggers-page">Triggers configuration page</a> and choose the appropriate tab (Comment, Taxonomy, etc.), where you can assign the action to run when the trigger event occurs.', array('@triggers-page' => url('admin/structure/trigger'), '@actions-page' => url('admin/config/system/actions'))) . '</dd>';
    $output .= '</dl>';
    return $output;
  }
}
```

---
_Drupal 7.103 · [modules/trigger/trigger.module](https://github.com/drupal/drupal/blob/7.103/modules/trigger/trigger.module) · Licensed GPL-2.0-or-later (see LICENSE)._
