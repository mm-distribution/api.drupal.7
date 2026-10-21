# LocaleCommentLanguageFunctionalTest::testCommentLanguage()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2956–3019 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2956-L3019)
- **Class:** [LocaleCommentLanguageFunctionalTest](../LocaleCommentLanguageFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testCommentLanguage()
```

## Documentation

```text
Test that comment language is properly set.
```

## Code

```php
  function testCommentLanguage() {
    drupal_static_reset('language_list');

    // Create two nodes, one for english and one for french, and comment each
    // node using both english and french as content language by changing URL
    // language prefixes. Meanwhile interface language is always French, which
    // is the user language preference. This way we can ensure that node
    // language and interface language do not influence comment language, as
    // only content language has to.
    foreach (language_list() as $node_langcode => $node_language) {
      $language_none = LANGUAGE_NONE;

      // Create "Article" content.
      $title = $this->randomName();
      $edit = array(
        "title" => $title,
        "body[$language_none][0][value]" => $this->randomName(),
        "language" => $node_langcode,
      );
      $this->drupalPost("node/add/article", $edit, t('Save'));
      $node = $this->drupalGetNodeByTitle($title);

      foreach (language_list() as $langcode => $language) {
        // Post a comment with content language $langcode.
        $prefix = empty($language->prefix) ? '' : $language->prefix . '/';
        $comment_values[$node_langcode][$langcode] = $this->randomName();
        // Initially field form widgets have no language.
        $edit = array(
          'subject' => $this->randomName(),
          "comment_body[$language_none][0][value]" => $comment_values[$node_langcode][$langcode],
        );
        $this->drupalPost("{$prefix}node/{$node->nid}", $edit, t('Preview'));
        // After the first submit the submitted entity language is taken into
        // account.
        $edit = array(
          'subject' => $edit['subject'],
          "comment_body[$langcode][0][value]" => $comment_values[$node_langcode][$langcode],
        );
        $this->drupalPost(NULL, $edit, t('Save'));

        // Check that comment language matches the current content language.
        $cid = db_select('comment', 'c')
          ->fields('c', array('cid'))
          ->condition('nid', $node->nid)
          ->orderBy('cid', 'DESC')
          ->range(0, 1)
          ->execute()
          ->fetchField();
        $comment = comment_load($cid);
        $comment_langcode = entity_language('comment', $comment);
        $args = array('%node_language' => $node_langcode, '%comment_language' => $comment_langcode, '%langcode' => $langcode);
        $this->assertEqual($comment_langcode, $langcode, format_string('The comment posted with content language %langcode and belonging to the node with language %node_language has language %comment_language', $args));
        $this->assertEqual($comment->comment_body[$langcode][0]['value'], $comment_values[$node_langcode][$langcode], 'Comment body correctly stored.');
      }
    }

    // Check that comment bodies appear in the administration UI.
    $this->drupalGet('admin/content/comment');
    foreach ($comment_values as $node_values) {
      foreach ($node_values as $value) {
        $this->assertRaw($value);
      }
    }
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
