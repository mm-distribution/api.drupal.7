# FileTokenReplaceTestCase::testFileTokenReplacement()

- **Type:** Method
- **File:** [`modules/file/tests/file.test`](../_file.md), lines 1497–1554 · [local source](../../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L1497-L1554)
- **Class:** [FileTokenReplaceTestCase](../FileTokenReplaceTestCase.md)
- **Module/theme:** file_module_test

## Signature

```php
function testFileTokenReplacement()
```

## Documentation

```text
Creates a file, then tests the tokens generated from it.
```

## Code

```php
  function testFileTokenReplacement() {
    global $language;
    $url_options = array(
      'absolute' => TRUE,
      'language' => $language,
    );

    // Create file field.
    $type_name = 'article';
    $field_name = 'field_' . strtolower($this->randomName());
    $this->createFileField($field_name, $type_name);
    $field = field_info_field($field_name);
    $instance = field_info_instance('node', $field_name, $type_name);

    $test_file = $this->getTestFile('text');
    // Coping a file to test uploads with non-latin filenames.
    $filename = drupal_dirname($test_file->uri) . '/текстовый файл.txt';
    $test_file = file_copy($test_file, $filename);

    // Create a new node with the uploaded file.
    $nid = $this->uploadNodeFile($test_file, $field_name, $type_name);

    // Load the node and the file.
    $node = node_load($nid, NULL, TRUE);
    $file = file_load($node->{$field_name}[LANGUAGE_NONE][0]['fid']);

    // Generate and test sanitized tokens.
    $tests = array();
    $tests['[file:fid]'] = $file->fid;
    $tests['[file:name]'] = check_plain($file->filename);
    $tests['[file:path]'] = check_plain($file->uri);
    $tests['[file:mime]'] = check_plain($file->filemime);
    $tests['[file:size]'] = format_size($file->filesize);
    $tests['[file:url]'] = check_plain(file_create_url($file->uri));
    $tests['[file:timestamp]'] = format_date($file->timestamp, 'medium', '', NULL, $language->language);
    $tests['[file:timestamp:short]'] = format_date($file->timestamp, 'short', '', NULL, $language->language);
    $tests['[file:owner]'] = check_plain(format_username($this->admin_user));
    $tests['[file:owner:uid]'] = $file->uid;

    // Test to make sure that we generated something for each token.
    $this->assertFalse(in_array(0, array_map('strlen', $tests)), 'No empty tokens generated.');

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('file' => $file), array('language' => $language));
      $this->assertEqual($output, $expected, format_string('Sanitized file token %token replaced.', array('%token' => $input)));
    }

    // Generate and test unsanitized tokens.
    $tests['[file:name]'] = $file->filename;
    $tests['[file:path]'] = $file->uri;
    $tests['[file:mime]'] = $file->filemime;
    $tests['[file:size]'] = format_size($file->filesize);

    foreach ($tests as $input => $expected) {
      $output = token_replace($input, array('file' => $file), array('language' => $language, 'sanitize' => FALSE));
      $this->assertEqual($output, $expected, format_string('Unsanitized file token %token replaced.', array('%token' => $input)));
    }
  }
```

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
