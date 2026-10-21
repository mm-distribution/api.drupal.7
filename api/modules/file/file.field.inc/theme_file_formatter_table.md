# theme_file_formatter_table()

- **Type:** Function
- **File:** [`modules/file/file.field.inc`](_file.md), lines 1017–1028 · [local source](../../../../source/modules/file/file.field.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc#L1017-L1028)
- **Module/theme:** file
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_file_formatter_table($variables)
```

## Documentation

```text
Returns HTML for a file attachments table.

@param $variables
  An associative array containing:
  - items: An array of file attachments.

@ingroup themeable
```

## Code

```php
function theme_file_formatter_table($variables) {
  $header = array(t('Attachment'), t('Size'));
  $rows = array();
  foreach ($variables['items'] as $delta => $item) {
    $rows[] = array(
      theme('file_link', array('file' => (object) $item)),
      format_size($item['filesize']),
    );
  }

  return empty($rows) ? '' : theme('table', array('header' => $header, 'rows' => $rows));
}
```

---
_Drupal 7.103 · [modules/file/file.field.inc](https://github.com/drupal/drupal/blob/7.103/modules/file/file.field.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
