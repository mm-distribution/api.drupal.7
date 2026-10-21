# FileFieldTestCase::removeNodeFile()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 157–164 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L157-L164)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function removeNodeFile($nid, $new_revision = TRUE)
```

## Documentation

```text
Removes a file from a node.

Note that if replacing a file, it must first be removed then added again.
```

## Code

```php
  function removeNodeFile($nid, $new_revision = TRUE) {
    $edit = array(
      'revision' => (string) (int) $new_revision,
    );

    $this->drupalPost('node/' . $nid . '/edit', array(), t('Remove'));
    $this->drupalPost(NULL, $edit, t('Save'));
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
