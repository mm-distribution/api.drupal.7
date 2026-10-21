# FileFieldTestCase::uploadNodeFile()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 124–150 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L124-L150)
- **Class:** [FileFieldTestCase](../FileFieldTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function uploadNodeFile($file, $field_name, $nid_or_type, $new_revision = TRUE, $extras = array())
```

## Documentation

```text
Uploads a file to a node.
```

## Code

```php
  function uploadNodeFile($file, $field_name, $nid_or_type, $new_revision = TRUE, $extras = array()) {
    $langcode = LANGUAGE_NONE;
    $edit = array(
      "title" => $this->randomName(),
      'revision' => (string) (int) $new_revision,
    );

    if (is_numeric($nid_or_type)) {
      $nid = $nid_or_type;
    }
    else {
      // Add a new node.
      $extras['type'] = $nid_or_type;
      $node = $this->drupalCreateNode($extras);
      $nid = $node->nid;
      // Save at least one revision to better simulate a real site.
      $this->drupalCreateNode(get_object_vars($node));
      $node = node_load($nid, NULL, TRUE);
      $this->assertNotEqual($nid, $node->vid, 'Node revision exists.');
    }

    // Attach a file to the node.
    $edit['files[' . $field_name . '_' . $langcode . '_0]'] = drupal_realpath($file->uri);
    $this->drupalPost("node/$nid/edit", $edit, t('Save'));

    return $nid;
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
