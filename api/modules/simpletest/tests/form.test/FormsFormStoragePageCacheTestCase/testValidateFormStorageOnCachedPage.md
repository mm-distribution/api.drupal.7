# FormsFormStoragePageCacheTestCase::testValidateFormStorageOnCachedPage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1481–1522 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1481-L1522)
- **Class:** [FormsFormStoragePageCacheTestCase](../FormsFormStoragePageCacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testValidateFormStorageOnCachedPage()
```

## Documentation

```text
Build-id is regenerated when validating cached form.
```

## Code

```php
  public function testValidateFormStorageOnCachedPage() {
    $this->drupalGet('form_test/form-storage-page-cache');
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'MISS', 'Page was not cached.');
    $this->assertText('No old build id', 'No old build id on the page');
    $build_id_initial = $this->getFormBuildId();

    // Trigger validation error by submitting an empty title.
    $edit = array('title' => '');
    $this->drupalPost(NULL, $edit, 'Save');
    $this->assertText($build_id_initial, 'Old build id on the page');
    $build_id_first_validation = $this->getFormBuildId();
    $this->assertNotEqual($build_id_initial, $build_id_first_validation, 'Build id changes when form validation fails');

    // Trigger validation error by again submitting an empty title.
    $edit = array('title' => '');
    $this->drupalPost(NULL, $edit, 'Save');
    $this->assertText('No old build id', 'No old build id on the page');
    $build_id_second_validation = $this->getFormBuildId();
    $this->assertEqual($build_id_first_validation, $build_id_second_validation, 'Build id remains the same when form validation fails subsequently');

    // Repeat the test sequence but this time with a page loaded from the cache.
    $this->drupalGet('form_test/form-storage-page-cache');
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'HIT', 'Page was cached.');
    $this->assertText('No old build id', 'No old build id on the page');
    $build_id_from_cache_initial = $this->getFormBuildId();
    $this->assertEqual($build_id_initial, $build_id_from_cache_initial, 'Build id is the same as on the first request');

    // Trigger validation error by submitting an empty title.
    $edit = array('title' => '');
    $this->drupalPost(NULL, $edit, 'Save');
    $this->assertText($build_id_initial, 'Old build id is initial build id');
    $build_id_from_cache_first_validation = $this->getFormBuildId();
    $this->assertNotEqual($build_id_initial, $build_id_from_cache_first_validation, 'Build id changes when form validation fails');
    $this->assertNotEqual($build_id_first_validation, $build_id_from_cache_first_validation, 'Build id from first user is not reused');

    // Trigger validation error by again submitting an empty title.
    $edit = array('title' => '');
    $this->drupalPost(NULL, $edit, 'Save');
    $this->assertText('No old build id', 'No old build id on the page');
    $build_id_from_cache_second_validation = $this->getFormBuildId();
    $this->assertEqual($build_id_from_cache_first_validation, $build_id_from_cache_second_validation, 'Build id remains the same when form validation fails subsequently');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
