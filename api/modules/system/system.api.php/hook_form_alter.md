# hook_form_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1671–1680 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1671-L1680)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_form_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Perform alterations before a form is rendered.

One popular use of this hook is to add form elements to the node form. When
altering a node form, the node object can be accessed at $form['#node'].

In addition to hook_form_alter(), which is called for all forms, there are
two more specific form hooks available. The first,
hook_form_BASE_FORM_ID_alter(), allows targeting of a form/forms via a base
form (if one exists). The second, hook_form_FORM_ID_alter(), can be used to
target a specific form directly.

The call order is as follows: all existing form alter functions are called
for module A, then all for module B, etc., followed by all for any base
theme(s), and finally for the theme itself. The module order is determined
by system weight, then by module name.

Within each module, form alter hooks are called in the following order:
first, hook_form_alter(); second, hook_form_BASE_FORM_ID_alter(); third,
hook_form_FORM_ID_alter(). So, for each module, the more general hooks are
called first followed by the more specific.

@param $form
  Nested array of form elements that comprise the form.
@param $form_state
  A keyed array containing the current state of the form. The arguments
  that drupal_get_form() was originally called with are available in the
  array $form_state['build_info']['args'].
@param $form_id
  String representing the name of the form itself. Typically this is the
  name of the function that generated the form.

@see hook_form_BASE_FORM_ID_alter()
@see hook_form_FORM_ID_alter()
@see forms_api_reference.html
```

## Code

```php
function hook_form_alter(&$form, &$form_state, $form_id) {
  if (isset($form['type']) && $form['type']['#value'] . '_node_settings' == $form_id) {
    $form['workflow']['upload_' . $form['type']['#value']] = array(
      '#type' => 'radios',
      '#title' => t('Attachments'),
      '#default_value' => variable_get('upload_' . $form['type']['#value'], 1),
      '#options' => array(t('Disabled'), t('Enabled')),
    );
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_form_alter()".

- [form_test_form_alter()](../../simpletest/tests/form_test.module/form_test_form_alter.md) — `modules/simpletest/tests/form_test.module`
- [taxonomy_test_form_alter()](../../simpletest/tests/taxonomy_test.module/taxonomy_test_form_alter.md) — `modules/simpletest/tests/taxonomy_test.module`
- [locale_form_alter()](../../locale/locale.module/locale_form_alter.md) — `modules/locale/locale.module`
- [overlay_form_alter()](../../overlay/overlay.module/overlay_form_alter.md) — `modules/overlay/overlay.module`
- [profile_form_alter()](../../profile/profile.module/profile_form_alter.md) — `modules/profile/profile.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
