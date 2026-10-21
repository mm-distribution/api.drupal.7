# ForumTestCase::testForum()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 119–253 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L119-L253)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
function testForum()
```

## Documentation

```text
Tests forum functionality through the admin and user interfaces.
```

## Code

```php
  function testForum() {
    //Check that the basic forum install creates a default forum topic
    $this->drupalGet("/forum");
    // Look for the "General discussion" default forum
    $this->assertText(t("General discussion"), "Found the default forum at the /forum listing");

    // Do the admin tests.
    $this->doAdminTests($this->admin_user);
    // Generate topics to populate the active forum block.
    $this->generateForumTopics($this->forum);

    // Login an unprivileged user to view the forum topics and generate an
    // active forum topics list.
    $this->drupalLogin($this->web_user);
    // Verify that this user is shown a message that they may not post content.
    $this->drupalGet('forum/' . $this->forum['tid']);
    $this->assertText(t('You are not allowed to post new content in the forum'), "Authenticated user without permission to post forum content is shown message in local tasks to that effect.");

    $this->viewForumTopics($this->nids);

    // Log in, and do basic tests for a user with permission to edit any forum
    // content.
    $this->doBasicTests($this->edit_any_topics_user, TRUE);
    // Create a forum node authored by this user.
    $any_topics_user_node = $this->createForumTopic($this->forum, FALSE);

    // Log in, and do basic tests for a user with permission to edit only its
    // own forum content.
    $this->doBasicTests($this->edit_own_topics_user, FALSE);
    // Create a forum node authored by this user.
    $own_topics_user_node = $this->createForumTopic($this->forum, FALSE);
    // Verify that this user cannot edit forum content authored by another user.
    $this->verifyForums($this->edit_any_topics_user, $any_topics_user_node, FALSE, 403);

    // Verify that this user is shown a local task to add new forum content.
    $this->drupalGet('forum');
    $this->assertLink(t('Add new Forum topic'));
    $this->drupalGet('forum/' . $this->forum['tid']);
    $this->assertLink(t('Add new Forum topic'));

    // Login a user with permission to edit any forum content.
    $this->drupalLogin($this->edit_any_topics_user);
    // Verify that this user can edit forum content authored by another user.
    $this->verifyForums($this->edit_own_topics_user, $own_topics_user_node, TRUE);

    // Verify the topic and post counts on the forum page.
    $this->drupalGet('forum');

    // Verify row for testing forum.
    $forum_arg = array(':forum' => 'forum-list-' . $this->forum['tid']);

    // Topics cell contains number of topics and number of unread topics.
    $xpath = $this->buildXPathQuery('//tr[@id=:forum]//td[@class="topics"]', $forum_arg);
    $topics = $this->xpath($xpath);
    $topics = trim($topics[0]);
    $this->assertEqual($topics, '6', 'Number of topics found.');

    // Verify the number of unread topics.
    $unread_topics = _forum_topics_unread($this->forum['tid'], $this->edit_any_topics_user->uid);
    $unread_topics = format_plural($unread_topics, '1 new', '@count new');
    $xpath = $this->buildXPathQuery('//tr[@id=:forum]//td[@class="topics"]//a', $forum_arg);
    $this->assertFieldByXPath($xpath, $unread_topics, 'Number of unread topics found.');

    // Verify total number of posts in forum.
    $xpath = $this->buildXPathQuery('//tr[@id=:forum]//td[@class="posts"]', $forum_arg);
    $this->assertFieldByXPath($xpath, '6', 'Number of posts found.');

    // Test loading multiple forum nodes on the front page.
    $this->drupalLogin($this->drupalCreateUser(array('administer content types', 'create forum content')));
    $this->drupalPost('admin/structure/types/manage/forum', array('node_options[promote]' => 'promote'), t('Save content type'));
    $this->createForumTopic($this->forum, FALSE);
    $this->createForumTopic($this->forum, FALSE);
    $this->drupalGet('node');

    // Test adding a comment to a forum topic.
    $node = $this->createForumTopic($this->forum, FALSE);
    $edit = array();
    $edit['comment_body[' . LANGUAGE_NONE . '][0][value]'] = $this->randomName();
    $this->drupalPost("node/$node->nid", $edit, t('Save'));
    $this->assertResponse(200);

    // Test editing a forum topic that has a comment.
    $this->drupalLogin($this->edit_any_topics_user);
    $this->drupalGet('forum/' . $this->forum['tid']);
    $this->drupalPost("node/$node->nid/edit", array(), t('Save'));
    $this->assertResponse(200);

    // Make sure constructing a forum node programmatically produces no notices.
    $node = new stdClass;
    $node->type = 'forum';
    $node->title = 'Test forum notices';
    $node->uid = 1;
    $node->taxonomy_forums[LANGUAGE_NONE][0]['tid'] = $this->root_forum['tid'];
    node_save($node);

    // Verify that adding taxonomy_forums reference field to another content
    // type does not trigger any errors.
    // Create new content type.
    $type_name = 'test_' . strtolower($this->randomName());
    $type = $this->drupalCreateContentType(array('name' => $type_name, 'type' => $type_name));
    // Create field instance on the bundle.
    $vocabulary = taxonomy_vocabulary_load(variable_get('forum_nav_vocabulary', 0));
    $instance = array(
      'field_name' => 'taxonomy_forums',
      'entity_type' => 'node',
      'label' => $vocabulary->name,
      'bundle' => $type->type,
      'required' => FALSE,
      'widget' => array(
        'type' => 'options_select',
      ),
      'display' => array(
        'default' => array(
          'type' => 'taxonomy_term_reference_link',
          'weight' => 10,
        ),
        'teaser' => array(
          'type' => 'taxonomy_term_reference_link',
          'weight' => 10,
        ),
      ),
    );
    field_create_instance($instance);
    // Create node and access node detail page.
    $settings = array(
      'type' => $type->type,
      'title' => $type_name,
      'taxonomy_forums' => array(LANGUAGE_NONE => array()),
    );
    $node1 = $this->drupalCreateNode($settings);
    $this->drupalGet('node/' . $node1->nid);
    $this->assertResponse(200);
    // Remove the field instance.
    field_delete_instance($instance);
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
