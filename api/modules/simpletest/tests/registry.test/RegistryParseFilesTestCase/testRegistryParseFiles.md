# RegistryParseFilesTestCase::testRegistryParseFiles()

- **Type:** Method
- **File:** [`modules/simpletest/tests/registry.test`](../_file.md), lines 105–117 · [local source](../../../../../../source/modules/simpletest/tests/registry.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test#L105-L117)
- **Class:** [RegistryParseFilesTestCase](../RegistryParseFilesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRegistryParseFiles()
```

## Documentation

```text
testRegistryParseFiles
```

## Code

```php
  function testRegistryParseFiles() {
    _registry_parse_files($this->getFiles());
    foreach ($this->fileTypes as $fileType) {
      // Test that we have all the right resources.
      foreach (array('className', 'interfaceName') as $resource) {
        $foundName = db_query('SELECT name FROM {registry} WHERE name = :name', array(':name' => $this->$fileType->$resource))->fetchField();
        $this->assertTrue($this->$fileType->$resource == $foundName, t('Resource "@resource" found.', array('@resource' => $this->$fileType->$resource)));
      }
      // Test that we have the right hash.
      $hash = db_query('SELECT hash FROM {registry_file} WHERE filename = :filename', array(':filename' => $this->$fileType->fileName))->fetchField();
      $this->assertTrue(hash('sha256', $this->$fileType->contents) == $hash, t('sha-256 for "@filename" matched.' . $fileType . $hash, array('@filename' => $this->$fileType->fileName)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/registry.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test) · Licensed GPL-2.0-or-later (see LICENSE)._
