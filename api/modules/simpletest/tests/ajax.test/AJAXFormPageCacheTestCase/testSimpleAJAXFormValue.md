# AJAXFormPageCacheTestCase::testSimpleAJAXFormValue()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 544–587 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L544-L587)
- **Class:** [AJAXFormPageCacheTestCase](../AJAXFormPageCacheTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testSimpleAJAXFormValue()
```

## Documentation

```text
Create a simple form, then POST to system/ajax to change to it.
```

## Code

```php
  public function testSimpleAJAXFormValue() {
    $this->drupalGet('ajax_forms_test_get_form');
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'MISS', 'Page was not cached.');
    $build_id_initial = $this->getFormBuildId();

    $edit = array('select' => 'green');
    $commands = $this->drupalPostAJAX(NULL, $edit, 'select');
    $build_id_first_ajax = $this->getFormBuildId();
    $this->assertNotEqual($build_id_initial, $build_id_first_ajax, 'Build id is changed in the simpletest-DOM on first AJAX submission');
    $expected = array(
      'command' => 'updateBuildId',
      'old' => $build_id_initial,
      'new' => $build_id_first_ajax,
    );
    $this->assertCommand($commands, $expected, 'Build id change command issued on first AJAX submission');

    $edit = array('select' => 'red');
    $commands = $this->drupalPostAJAX(NULL, $edit, 'select');
    $build_id_second_ajax = $this->getFormBuildId();
    $this->assertEqual($build_id_first_ajax, $build_id_second_ajax, 'Build id remains the same on subsequent AJAX submissions');

    // Repeat the test sequence but this time with a page loaded from the cache.
    $this->drupalGet('ajax_forms_test_get_form');
    $this->assertEqual($this->drupalGetHeader('X-Drupal-Cache'), 'HIT', 'Page was cached.');
    $build_id_from_cache_initial = $this->getFormBuildId();
    $this->assertEqual($build_id_initial, $build_id_from_cache_initial, 'Build id is the same as on the first request');

    $edit = array('select' => 'green');
    $commands = $this->drupalPostAJAX(NULL, $edit, 'select');
    $build_id_from_cache_first_ajax = $this->getFormBuildId();
    $this->assertNotEqual($build_id_from_cache_initial, $build_id_from_cache_first_ajax, 'Build id is changed in the simpletest-DOM on first AJAX submission');
    $this->assertNotEqual($build_id_first_ajax, $build_id_from_cache_first_ajax, 'Build id from first user is not reused');
    $expected = array(
      'command' => 'updateBuildId',
      'old' => $build_id_from_cache_initial,
      'new' => $build_id_from_cache_first_ajax,
    );
    $this->assertCommand($commands, $expected, 'Build id change command issued on first AJAX submission');

    $edit = array('select' => 'red');
    $commands = $this->drupalPostAJAX(NULL, $edit, 'select');
    $build_id_from_cache_second_ajax = $this->getFormBuildId();
    $this->assertEqual($build_id_from_cache_first_ajax, $build_id_from_cache_second_ajax, 'Build id remains the same on subsequent AJAX submissions');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
