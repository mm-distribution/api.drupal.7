# RegistryParseFileTestCase::testRegistryParseFile()

- **Type:** Method
- **File:** [`modules/simpletest/tests/registry.test`](../_file.md), lines 27–33 · [local source](../../../../../../source/modules/simpletest/tests/registry.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test#L27-L33)
- **Class:** [RegistryParseFileTestCase](../RegistryParseFileTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testRegistryParseFile()
```

## Documentation

```text
testRegistryParseFile
```

## Code

```php
  function testRegistryParseFile() {
    _registry_parse_file($this->fileName, $this->getFileContents());
    foreach (array('className', 'interfaceName') as $resource) {
      $foundName = db_query('SELECT name FROM {registry} WHERE name = :name', array(':name' => $this->$resource))->fetchField();
      $this->assertTrue($this->$resource == $foundName, t('Resource "@resource" found.', array('@resource' => $this->$resource)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/registry.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/registry.test) · Licensed GPL-2.0-or-later (see LICENSE)._
