# PathLookupTest::testDrupalLookupPath()

- **Type:** Method
- **File:** [`modules/simpletest/tests/path.test`](../_file.md), lines 262–345 · [local source](../../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L262-L345)
- **Class:** [PathLookupTest](../PathLookupTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalLookupPath()
```

## Documentation

```text
Test that drupal_lookup_path() returns the correct path.
```

## Code

```php
  function testDrupalLookupPath() {
    $account = $this->drupalCreateUser();
    $uid = $account->uid;
    $name = $account->name;

    // Test the situation where the source is the same for multiple aliases.
    // Start with a language-neutral alias, which we will override.
    $path = array(
      'source' => "user/$uid",
      'alias' => 'foo',
    );
    path_save($path);
    $this->assertEqual(drupal_lookup_path('alias', $path['source']), $path['alias'], 'Basic alias lookup works.');
    $this->assertEqual(drupal_lookup_path('source', $path['alias']), $path['source'], 'Basic source lookup works.');

    // Create a language specific alias for the default language (English).
    $path = array(
      'source' => "user/$uid",
      'alias' => "users/$name",
      'language' => 'en',
    );
    path_save($path);
    $this->assertEqual(drupal_lookup_path('alias', $path['source']), $path['alias'], 'English alias overrides language-neutral alias.');
    $this->assertEqual(drupal_lookup_path('source', $path['alias']), $path['source'], 'English source overrides language-neutral source.');

    // Create a language-neutral alias for the same path, again.
    $path = array(
      'source' => "user/$uid",
      'alias' => 'bar',
    );
    path_save($path);
    $this->assertEqual(drupal_lookup_path('alias', $path['source']), "users/$name", 'English alias still returned after entering a language-neutral alias.');

    // Create a language-specific (xx-lolspeak) alias for the same path.
    $path = array(
      'source' => "user/$uid",
      'alias' => 'LOL',
      'language' => 'xx-lolspeak',
    );
    path_save($path);
    $this->assertEqual(drupal_lookup_path('alias', $path['source']), "users/$name", 'English alias still returned after entering a LOLspeak alias.');
    // The LOLspeak alias should be returned if we really want LOLspeak.
    $this->assertEqual(drupal_lookup_path('alias', $path['source'], 'xx-lolspeak'), 'LOL', 'LOLspeak alias returned if we specify xx-lolspeak to drupal_lookup_path().');

    // Create a new alias for this path in English, which should override the
    // previous alias for "user/$uid".
    $path = array(
      'source' => "user/$uid",
      'alias' => 'users/my-new-path',
      'language' => 'en',
    );
    path_save($path);
    $this->assertEqual(drupal_lookup_path('alias', $path['source']), $path['alias'], 'Recently created English alias returned.');
    $this->assertEqual(drupal_lookup_path('source', $path['alias']), $path['source'], 'Recently created English source returned.');

    // Remove the English aliases, which should cause a fallback to the most
    // recently created language-neutral alias, 'bar'.
    db_delete('url_alias')
      ->condition('language', 'en')
      ->execute();
    drupal_clear_path_cache();
    $this->assertEqual(drupal_lookup_path('alias', $path['source']), 'bar', 'Path lookup falls back to recently created language-neutral alias.');

    // Test the situation where the alias and language are the same, but
    // the source differs. The newer alias record should be returned.
    $account2 = $this->drupalCreateUser();
    $path = array(
      'source' => 'user/' . $account2->uid,
      'alias' => 'bar',
    );
    path_save($path);
    $this->assertEqual(drupal_lookup_path('source', $path['alias']), $path['source'], 'Newer alias record is returned when comparing two LANGUAGE_NONE paths with the same alias.');

    // Test if the alias returned by drupal_lookup_path() is the same as the
    // alias returned by path_load().
    $path = array(
      'source' => 'user/' . $account2->uid,
      'alias' => 'bar2',
    );
    path_save($path);
    $this->assertEqual(drupal_lookup_path('alias', $path['source']), 'bar2', 'Newer alias record is returned when using drupal_lookup_path() on paths with multiple aliases.');
    $loaded_path = path_load(array('source' => $path['source']));
    $this->assertEqual($loaded_path['alias'], 'bar2', 'Newer alias record is returned when using path_load() on paths with multiple aliases.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
