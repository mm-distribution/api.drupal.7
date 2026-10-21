# DrupalRenderTestCase::testDrupalRenderCache()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 2412–2491 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2412-L2491)
- **Class:** [DrupalRenderTestCase](../DrupalRenderTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalRenderCache()
```

## Documentation

```text
Tests caching of render items.
```

## Code

```php
  function testDrupalRenderCache() {
    // Force a request via GET.
    $request_method = $_SERVER['REQUEST_METHOD'];
    $_SERVER['REQUEST_METHOD'] = 'GET';
    // Create an empty element.
    $test_element = array(
      '#cache' => array(
        'cid' => 'render_cache_test',
      ),
      '#markup' => '',
    );

    // Render the element and confirm that it goes through the rendering
    // process (which will set $element['#printed']).
    $element = $test_element;
    drupal_render($element);
    $this->assertTrue(isset($element['#printed']), 'No cache hit');

    // Render the element again and confirm that it is retrieved from the cache
    // instead (so $element['#printed'] will not be set).
    $element = $test_element;
    drupal_render($element);
    $this->assertFalse(isset($element['#printed']), 'Cache hit');

    // Test that user 1 does not share the cache with other users who have the
    // same roles, even when DRUPAL_CACHE_PER_ROLE is used.
    $user1 = user_load(1);
    $first_authenticated_user = $this->drupalCreateUser();
    $second_authenticated_user = $this->drupalCreateUser();
    $user1->roles = array_intersect_key($user1->roles, array(DRUPAL_AUTHENTICATED_RID => TRUE));
    user_save($user1);
    // Load all the accounts again, to make sure we have complete account
    // objects.
    $user1 = user_load(1);
    $first_authenticated_user = user_load($first_authenticated_user->uid);
    $second_authenticated_user = user_load($second_authenticated_user->uid);
    $this->assertEqual($user1->roles, $first_authenticated_user->roles, 'User 1 has the same roles as an authenticated user.');
    // Impersonate user 1 and render content that only user 1 should have
    // permission to see.
    $original_user = $GLOBALS['user'];
    $original_session_state = drupal_save_session();
    drupal_save_session(FALSE);
    $GLOBALS['user'] = $user1;
    $test_element = array(
      '#cache' => array(
        'keys' => array('test'),
        'granularity' => DRUPAL_CACHE_PER_ROLE,
      ),
    );
    $element = $test_element;
    $element['#markup'] = 'content for user 1';
    $output = drupal_render($element);
    $this->assertEqual($output, 'content for user 1');
    // Verify the cache is working by rendering the same element but with
    // different markup passed in; the result should be the same.
    $element = $test_element;
    $element['#markup'] = 'should not be used';
    $output = drupal_render($element);
    $this->assertEqual($output, 'content for user 1');
    // Verify that the first authenticated user does not see the same content
    // as user 1.
    $GLOBALS['user'] = $first_authenticated_user;
    $element = $test_element;
    $element['#markup'] = 'content for authenticated users';
    $output = drupal_render($element);
    $this->assertEqual($output, 'content for authenticated users');
    // Verify that the second authenticated user shares the cache with the
    // first authenticated user.
    $GLOBALS['user'] = $second_authenticated_user;
    $element = $test_element;
    $element['#markup'] = 'should not be used';
    $output = drupal_render($element);
    $this->assertEqual($output, 'content for authenticated users');
    // Restore the original logged-in user.
    $GLOBALS['user'] = $original_user;
    drupal_save_session($original_session_state);

    // Restore the previous request method.
    $_SERVER['REQUEST_METHOD'] = $request_method;
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
