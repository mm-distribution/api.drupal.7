# FileFieldTestCase::replaceNodeFile()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 169–177 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L169-L177)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function replaceNodeFile($file, $field_name, $nid, $new_revision = TRUE)
```

## Documentation

```text
Replaces a file within a node.
```

## Code

```php
  function replaceNodeFile($file, $field_name, $nid, $new_revision = TRUE) {
    $edit = array(
      'files[' . $field_name . '_' . LANGUAGE_NONE . '_0]' => drupal_realpath($file->uri),
      'revision' => (string) (int) $new_revision,
    );

    $this->drupalPost('node/' . $nid . '/edit', array(), t('Remove'));
    $this->drupalPost(NULL, $edit, t('Save'));
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
