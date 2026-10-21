# FileTaxonomyTermTestCase::_testTermFile()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 329–366 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L329-L366)
- **Class:** [FileTaxonomyTermTestCase](../FileTaxonomyTermTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
protected function _testTermFile($uri_scheme)
```

## Documentation

```text
Runs tests for attaching a file field to a taxonomy term.

@param $uri_scheme
  The URI scheme to use for the file field, either "public" or "private".
```

## Code

```php
  protected function _testTermFile($uri_scheme) {
    $field_name = strtolower($this->randomName());
    $this->createAttachFileField($field_name, $uri_scheme);
    // Get a file to upload.
    $file = current($this->drupalGetTestFiles('text'));
    // Add a filesize property to files as would be read by file_load().
    $file->filesize = filesize($file->uri);
    $langcode = LANGUAGE_NONE;
    $edit = array(
      "name" => $this->randomName(),
    );
    // Attach a file to the term.
    $edit['files[' . $field_name . '_' . $langcode . '_0]'] = drupal_realpath($file->uri);
    $this->drupalPost("admin/structure/taxonomy/tags/add", $edit, t('Save'));
    // Find the term ID we just created.
    $tid = db_query_range('SELECT tid FROM {taxonomy_term_data} ORDER BY tid DESC', 0, 1)->fetchField();
    $terms = entity_load('taxonomy_term', array($tid));
    $term = $terms[$tid];
    $fid = $term->{$field_name}[LANGUAGE_NONE][0]['fid'];
    // Check that the uploaded file is present on the edit form.
    $this->drupalGet("taxonomy/term/$tid/edit");
    $file_input_name = $field_name . '[' . LANGUAGE_NONE . '][0][fid]';
    $this->assertFieldByXpath('//input[@type="hidden" and @name="' . $file_input_name . '"]', $fid, 'File is attached on edit form.');
    // Edit the term and change name without changing the file.
    $edit = array(
      "name" => $this->randomName(),
    );
    $this->drupalPost("taxonomy/term/$tid/edit", $edit, t('Save'));
    // Check that the uploaded file is still present on the edit form.
    $this->drupalGet("taxonomy/term/$tid/edit");
    $file_input_name = $field_name . '[' . LANGUAGE_NONE . '][0][fid]';
    $this->assertFieldByXpath('//input[@type="hidden" and @name="' . $file_input_name . '"]', $fid, 'File is attached on edit form.');
    // Load term while resetting the cache.
    $terms = entity_load('taxonomy_term', array($tid), array(), TRUE);
    $term = $terms[$tid];
    $this->assertTrue(!empty($term->{$field_name}[LANGUAGE_NONE]), 'Term has attached files.');
    $this->assertEqual($term->{$field_name}[LANGUAGE_NONE][0]['fid'], $fid, 'Same File ID is attached to the term.');
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
