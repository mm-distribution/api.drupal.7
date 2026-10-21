# PathSaveTest::testDrupalSaveOriginalPath()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 369–391 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L369-L391)
- **Class:** [PathSaveTest](../PathSaveTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalSaveOriginalPath()
```

## Documentation

```text
Tests that path_save() makes the original path available to modules.
```

## Code

```php
  function testDrupalSaveOriginalPath() {
    $account = $this->drupalCreateUser();
    $uid = $account->uid;
    $name = $account->name;

    // Create a language-neutral alias.
    $path = array(
      'source' => "user/$uid",
      'alias' => 'foo',
    );
    $path_original = $path;
    path_save($path);

    // Alter the path.
    $path['alias'] = 'bar';
    path_save($path);

    // Test to see if the original alias is available to modules during
    // hook_path_update().
    $results = variable_get('path_test_results', array());
    $this->assertIdentical($results['hook_path_update']['original']['alias'], $path_original['alias'], 'Old path alias available to modules during hook_path_update.');
    $this->assertIdentical($results['hook_path_update']['original']['source'], $path_original['source'], 'Old path alias available to modules during hook_path_update.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
