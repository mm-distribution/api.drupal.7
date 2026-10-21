# RegistryParseFilesTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/registry.test`](../_file.md), lines 65–100 · [local source](../../../../../../source/modules/simpletest/tests/registry.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test#L65-L100)
- **Class:** [RegistryParseFilesTestCase](../RegistryParseFilesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();
    // Create files with some php to parse - one 'new', one 'existing' so
    // we test all the important code paths in _registry_parse_files.
    foreach ($this->fileTypes as $fileType) {
      $chrs = hash('sha256', microtime() . mt_rand());
      $this->$fileType = new stdClass();
      $this->$fileType->fileName = 'public://registry_test_' . substr($chrs, 0, 16);
      $this->$fileType->className = 'registry_test_class' . substr($chrs, 16, 16);
      $this->$fileType->interfaceName = 'registry_test_interface' . substr($chrs, 32, 16);
      $this->$fileType->contents = $this->getFileContents($fileType);
      file_save_data($this->$fileType->contents, $this->$fileType->fileName);

      if ($fileType == 'existing_changed') {
        // Add a record with an incorrect hash.
        $this->$fileType->fakeHash = hash('sha256', mt_rand());
        db_insert('registry_file')
          ->fields(array(
            'hash' => $this->$fileType->fakeHash,
            'filename' => $this->$fileType->fileName,
          ))
          ->execute();

        // Insert some fake resource records.
        foreach (array('class', 'interface') as $type) {
          db_insert('registry')
            ->fields(array(
              'name' => $type . hash('sha256', microtime() . mt_rand()),
              'type' => $type,
              'filename' => $this->$fileType->fileName,
            ))
            ->execute();
        }
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/registry.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test) · Licensed GPL-2.0-or-later (see LICENSE)._
