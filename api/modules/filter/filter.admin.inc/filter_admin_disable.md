# filter_admin_disable()

- **Type:** Function
- **File:** [`modules/filter/filter.admin.inc`](_file.md), lines 388–397 · [local source](../../../../source/modules/filter/filter.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc#L388-L397)
- **Module/theme:** filter
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function filter_admin_disable($form, &$form_state, $format)
```

## Documentation

```text
Form constructor for the text format deletion confirmation form.

@param $format
  An object representing a text format.

@see filter_menu()
@see filter_admin_disable_submit()
@ingroup forms
```

## Code

```php
function filter_admin_disable($form, &$form_state, $format) {
  $form['#format'] = $format;

  return confirm_form($form,
    t('Are you sure you want to disable the text format %format?', array('%format' => $format->name)),
    'admin/config/content/formats',
    t('Disabled text formats are completely removed from the administrative interface, and any content stored with that format will not be displayed. This action cannot be undone.'),
    t('Disable')
  );
}
```

---
_Drupal 7.103 · [modules/filter/filter.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
