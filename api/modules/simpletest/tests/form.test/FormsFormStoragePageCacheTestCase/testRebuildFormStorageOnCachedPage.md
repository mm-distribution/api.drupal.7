# FormsFormStoragePageCacheTestCase::testRebuildFormStorageOnCachedPage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1527–1546 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1527-L1546)
- **Class:** [FormsFormStoragePageCacheTestCase](../FormsFormStoragePageCacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testRebuildFormStorageOnCachedPage()
```

## Documentation

```text
Build-id is regenerated when rebuilding cached form.
```

## Code

```php
  public function testRebuildFormStorageOnCachedPage() {
    $this->drupalGet('form_test/form-storage-page-cache');
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'MISS', 'Page was not cached.');
    $this->assertText('No old build id', 'No old build id on the page');
    $build_id_initial = $this->getFormBuildId();

    // Trigger rebuild, should regenerate build id.
    $edit = array('title' => 'something');
    $this->drupalPost(NULL, $edit, 'Rebuild');
    $this->assertText($build_id_initial, 'Initial build id as old build id on the page');
    $build_id_first_rebuild = $this->getFormBuildId();
    $this->assertNotEqual($build_id_initial, $build_id_first_rebuild, 'Build id changes on first rebuild.');

    // Trigger subsequent rebuild, should regenerate the build id again.
    $edit = array('title' => 'something');
    $this->drupalPost(NULL, $edit, 'Rebuild');
    $this->assertText($build_id_first_rebuild, 'First build id as old build id on the page');
    $build_id_second_rebuild = $this->getFormBuildId();
    $this->assertNotEqual($build_id_first_rebuild, $build_id_second_rebuild, 'Build id changes on second rebuild.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
