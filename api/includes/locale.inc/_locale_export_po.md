# _locale_export_po()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1785–1800 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1785-L1800)
- **Topics:** [locale-api-import-export](../../topics/locale-api-import-export.md)

## Signature

```php
function _locale_export_po($language = NULL, $output = NULL)
```

## Documentation

```text
Write a generated PO or POT file to the output.

@param $language
  Language object to generate the output for, or NULL if generating
  translation template.
@param $output
  The PO(T) file to output as a string. See _locale_export_generate_po()
  on how it can be generated.
```

## Code

```php
function _locale_export_po($language = NULL, $output = NULL) {
  // Log the export event.
  if (isset($language)) {
    $filename = $language->language . '.po';
    watchdog('locale', 'Exported %locale translation file: %filename.', array('%locale' => $language->name, '%filename' => $filename));
  }
  else {
    $filename = 'drupal.pot';
    watchdog('locale', 'Exported translation file: %filename.', array('%filename' => $filename));
  }
  // Download the file for the client.
  header("Content-Disposition: attachment; filename=$filename");
  header("Content-Type: text/plain; charset=utf-8");
  print $output;
  drupal_exit();
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
