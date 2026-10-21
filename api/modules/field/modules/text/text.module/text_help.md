# text_help()

- **Type:** Function
- **File:** [`modules/field/modules/text/text.module`](_file.md), lines 11–19 · [local source](../../../../../../source/modules/field/modules/text/text.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module#L11-L19)
- **Module/theme:** text
- **Implements:** [hook_help()](../../../../system/system.api.php/hook_help.md)

## Signature

```php
function text_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function text_help($path, $arg) {
  switch ($path) {
    case 'admin/help#text':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t("The Text module defines various text field types for the Field module. A text field may contain plain text only, or optionally, may use Drupal's <a href='@filter-help'>text filters</a> to securely manage HTML output. Text input fields may be either a single line (text field), multiple lines (text area), or for greater input control, a select box, checkbox, or radio buttons. If desired, the field can be validated, so that it is limited to a set of allowed values. See the <a href='@field-help'>Field module help page</a> for more information about fields.", array('@field-help' => url('admin/help/field'), '@filter-help' => url('admin/help/filter'))) . '</p>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/field/modules/text/text.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.module) · Licensed GPL-2.0-or-later (see LICENSE)._
