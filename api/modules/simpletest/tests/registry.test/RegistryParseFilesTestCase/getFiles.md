# RegistryParseFilesTestCase::getFiles()

- **Type:** Method
- **File:** [`modules/simpletest/tests/registry.test`](../_file.md), lines 122–131 · [local source](../../../../../../source/modules/simpletest/tests/registry.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test#L122-L131)
- **Class:** [RegistryParseFilesTestCase](../RegistryParseFilesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function getFiles()
```

## Documentation

```text
getFiles
```

## Code

```php
  function getFiles() {
    $files = array();
    foreach ($this->fileTypes as $fileType) {
      $files[$this->$fileType->fileName] = array('module' => '', 'weight' => 0);
      if ($fileType == 'existing_changed') {
        $files[$this->$fileType->fileName]['hash'] = $this->$fileType->fakeHash;
      }
    }
    return $files;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/registry.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test) · Licensed GPL-2.0-or-later (see LICENSE)._
