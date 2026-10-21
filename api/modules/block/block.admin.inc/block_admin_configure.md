# block_admin_configure()

- **Type:** Function
- **File:** [`modules/block/block.admin.inc`](_file.md), lines 255–440 · [local source](../../../../source/modules/block/block.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc#L255-L440)
- **Module/theme:** block
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function block_admin_configure($form, &$form_state, $module, $delta)
```

## Documentation

```text
Form constructor for the block configuration form.

Also used by block_add_block_form() for adding a new custom block.

@param $module
  Name of the module that implements the block to be configured.
@param $delta
  Unique ID of the block within the context of $module.

@see block_admin_configure_validate()
@see block_admin_configure_submit()
@ingroup forms
```

## Code

```php
function block_admin_configure($form, &$form_state, $module, $delta) {
  $block = block_load($module, $delta);
  $form['module'] = array(
    '#type' => 'value',
    '#value' => $block->module,
  );
  $form['delta'] = array(
    '#type' => 'value',
    '#value' => $block->delta,
  );

  // Get the block subject for the page title.
  $info = module_invoke($block->module, 'block_info');
  if (isset($info[$block->delta])) {
    drupal_set_title(t("'%name' block", array('%name' => $info[$block->delta]['info'])), PASS_THROUGH);
  }

  $form['settings']['title'] = array(
    '#type' => 'textfield',
    '#title' => t('Block title'),
    '#maxlength' => 255,
    '#description' => $block->module == 'block' ? t('The title of the block as shown to the user.') : t('Override the default title for the block. Use <em>!placeholder</em> to display no title, or leave blank to use the default block title.', array('!placeholder' => '&lt;none&gt;')),
    '#default_value' => isset($block->title) ? $block->title : '',
    '#weight' => -19,
  );

  // Module-specific block configuration.
  if ($settings = module_invoke($block->module, 'block_configure', $block->delta)) {
    foreach ($settings as $k => $v) {
      $form['settings'][$k] = $v;
    }
  }

  // Region settings.
  $form['regions'] = array(
    '#type' => 'fieldset',
    '#title' => t('Region settings'),
    '#collapsible' => FALSE,
    '#description' => t('Specify in which themes and regions this block is displayed.'),
    '#tree' => TRUE,
  );

  $theme_default = variable_get('theme_default', 'bartik');
  $admin_theme = variable_get('admin_theme');
  foreach (list_themes() as $key => $theme) {
    // Only display enabled themes
    if ($theme->status) {
      $region = db_query("SELECT region FROM {block} WHERE module = :module AND delta = :delta AND theme = :theme", array(
        ':module' => $block->module,
        ':delta' => $block->delta,
        ':theme' => $key,
      ))->fetchField();

      // Use a meaningful title for the main site theme and administrative
      // theme.
      $theme_title = $theme->info['name'];
      if ($key == $theme_default) {
        $theme_title = t('!theme (default theme)', array('!theme' => $theme_title));
      }
      elseif ($admin_theme && $key == $admin_theme) {
        $theme_title = t('!theme (administration theme)', array('!theme' => $theme_title));
      }
      $form['regions'][$key] = array(
        '#type' => 'select',
        '#title' => $theme_title,
        '#default_value' => !empty($region) && $region != -1 ? $region : NULL,
        '#empty_value' => BLOCK_REGION_NONE,
        '#options' => system_region_list($key, REGIONS_VISIBLE),
        '#weight' => ($key == $theme_default ? 9 : 10),
      );
    }
  }

  // Visibility settings.
  $form['visibility_title'] = array(
    '#type' => 'item',
    '#title' => t('Visibility settings'),
  );
  $form['visibility'] = array(
    '#type' => 'vertical_tabs',
    '#attached' => array(
      'js' => array(drupal_get_path('module', 'block') . '/block.js'),
    ),
  );

  // Per-path visibility.
  $form['visibility']['path'] = array(
    '#type' => 'fieldset',
    '#title' => t('Pages'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#group' => 'visibility',
    '#weight' => 0,
  );

  $access = user_access('use PHP for settings');
  if (isset($block->visibility) && $block->visibility == BLOCK_VISIBILITY_PHP && !$access) {
    $form['visibility']['path']['visibility'] = array(
      '#type' => 'value',
      '#value' => BLOCK_VISIBILITY_PHP,
    );
    $form['visibility']['path']['pages'] = array(
      '#type' => 'value',
      '#value' => isset($block->pages) ? $block->pages : '',
    );
  }
  else {
    $options = array(
      BLOCK_VISIBILITY_NOTLISTED => t('All pages except those listed'),
      BLOCK_VISIBILITY_LISTED => t('Only the listed pages'),
    );
    $description = t("Specify pages by using their paths. Enter one path per line. The '*' character is a wildcard. Example paths are %blog for the blog page and %blog-wildcard for every personal blog. %front is the front page.", array('%blog' => 'blog', '%blog-wildcard' => 'blog/*', '%front' => '<front>'));

    if (module_exists('php') && $access) {
      $options += array(BLOCK_VISIBILITY_PHP => t('Pages on which this PHP code returns <code>TRUE</code> (experts only)'));
      $title = t('Pages or PHP code');
      $description .= ' ' . t('If the PHP option is chosen, enter PHP code between %php. Note that executing incorrect PHP code can break your Drupal site.', array('%php' => '<?php ?>'));
    }
    else {
      $title = t('Pages');
    }
    $form['visibility']['path']['visibility'] = array(
      '#type' => 'radios',
      '#title' => t('Show block on specific pages'),
      '#options' => $options,
      '#default_value' => isset($block->visibility) ? $block->visibility : BLOCK_VISIBILITY_NOTLISTED,
    );
    $form['visibility']['path']['pages'] = array(
      '#type' => 'textarea',
      '#title' => '<span class="element-invisible">' . $title . '</span>',
      '#default_value' => isset($block->pages) ? $block->pages : '',
      '#description' => $description,
    );
  }

  // Per-role visibility.
  $default_role_options = db_query("SELECT rid FROM {block_role} WHERE module = :module AND delta = :delta", array(
    ':module' => $block->module,
    ':delta' => $block->delta,
  ))->fetchCol();
  $role_options = array_map('check_plain', user_roles());
  $form['visibility']['role'] = array(
    '#type' => 'fieldset',
    '#title' => t('Roles'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#group' => 'visibility',
    '#weight' => 10,
  );
  $form['visibility']['role']['roles'] = array(
    '#type' => 'checkboxes',
    '#title' => t('Show block for specific roles'),
    '#default_value' => $default_role_options,
    '#options' => $role_options,
    '#description' => t('Show this block only for the selected role(s). If you select no roles, the block will be visible to all users.'),
  );

  // Per-user visibility.
  $form['visibility']['user'] = array(
    '#type' => 'fieldset',
    '#title' => t('Users'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#group' => 'visibility',
    '#weight' => 20,
  );
  $form['visibility']['user']['custom'] = array(
    '#type' => 'radios',
    '#title' => t('Customizable per user'),
    '#options' => array(
      BLOCK_CUSTOM_FIXED => t('Not customizable'),
      BLOCK_CUSTOM_ENABLED => t('Customizable, visible by default'),
      BLOCK_CUSTOM_DISABLED => t('Customizable, hidden by default'),
    ),
    '#description' => t('Allow individual users to customize the visibility of this block in their account settings.'),
    '#default_value' => isset($block->custom) ? $block->custom : BLOCK_CUSTOM_FIXED,
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save block'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/block/block.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/block/block.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
