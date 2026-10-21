# system_goto_action_form()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 3363–3372 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L3363-L3372)
- **Module/theme:** system

## Signature

```php
function system_goto_action_form($context)
```

## Documentation

```text
Settings form for system_goto_action().
```

## Code

```php
function system_goto_action_form($context) {
  $form['url'] = array(
    '#type' => 'textfield',
    '#title' => t('URL'),
    '#description' => t('The URL to which the user should be redirected. This can be an internal path like node/1234 or an external URL like http://example.com.'),
    '#default_value' => isset($context['url']) ? $context['url'] : '',
    '#required' => TRUE,
  );
  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
