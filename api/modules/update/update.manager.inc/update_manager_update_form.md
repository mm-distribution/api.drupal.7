# update_manager_update_form()

- **Type:** Function
- **File:** [`modules/update/update.manager.inc`](_file.md), lines 62–265 · [local source](../../../../source/modules/update/update.manager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc#L62-L265)
- **Module/theme:** update
- **Topics:** [update_manager_update](../../../topics/update_manager_update.md), [forms](../../../topics/forms.md)

## Signature

```php
function update_manager_update_form($form, $form_state, $context)
```

## Documentation

```text
Form constructor for the update form of the Update Manager module.

This presents a table with all projects that have available updates with
checkboxes to select which ones to upgrade.

@param $context
  String representing the context from which we're trying to update.
  Allowed values are 'module', 'theme', and 'report'.

@see update_manager_update_form_validate()
@see update_manager_update_form_submit()
@see update_menu()
@ingroup forms
```

## Code

```php
function update_manager_update_form($form, $form_state, $context) {
  if (!_update_manager_check_backends($form, 'update')) {
    return $form;
  }

  $form['#theme'] = 'update_manager_update_form';

  $available = update_get_available(TRUE);
  if (empty($available)) {
    $form['message'] = array(
      '#markup' => t('There was a problem getting update information. Try again later.'),
    );
    return $form;
  }

  $form['#attached']['css'][] = drupal_get_path('module', 'update') . '/update.css';

  // This will be a nested array. The first key is the kind of project, which
  // can be either 'enabled', 'disabled', 'manual' (projects which require
  // manual updates, such as core). Then, each subarray is an array of
  // projects of that type, indexed by project short name, and containing an
  // array of data for cells in that project's row in the appropriate table.
  $projects = array();

  // This stores the actual download link we're going to update from for each
  // project in the form, regardless of if it's enabled or disabled.
  $form['project_downloads'] = array('#tree' => TRUE);

  module_load_include('inc', 'update', 'update.compare');
  $project_data = update_calculate_project_data($available);
  foreach ($project_data as $name => $project) {
    // Filter out projects which are up to date already.
    if ($project['status'] == UPDATE_CURRENT) {
      continue;
    }
    // The project name to display can vary based on the info we have.
    if (!empty($project['title'])) {
      if (!empty($project['link'])) {
        $project_name = l($project['title'], $project['link']);
      }
      else {
        $project_name = check_plain($project['title']);
      }
    }
    elseif (!empty($project['info']['name'])) {
      $project_name = check_plain($project['info']['name']);
    }
    else {
      $project_name = check_plain($name);
    }
    if ($project['project_type'] == 'theme' || $project['project_type'] == 'theme-disabled') {
      $project_name .= ' ' . t('(Theme)');
    }

    if (empty($project['recommended'])) {
      // If we don't know what to recommend they upgrade to, we should skip
      // the project entirely.
      continue;
    }

    $recommended_release = $project['releases'][$project['recommended']];
    $recommended_version = $recommended_release['version'] . ' ' . l(t('(Release notes)'), $recommended_release['release_link'], array('attributes' => array('title' => t('Release notes for @project_title', array('@project_title' => $project['title'])))));
    if ($recommended_release['version_major'] != $project['existing_major']) {
      $recommended_version .= '<div title="Major upgrade warning" class="update-major-version-warning">' . t('This update is a major version update which means that it may not be backwards compatible with your currently running version.  It is recommended that you read the release notes and proceed at your own risk.') . '</div>';
    }

    // Create an entry for this project.
    $entry = array(
      'title' => $project_name,
      'installed_version' => $project['existing_version'],
      'recommended_version' => $recommended_version,
    );

    switch ($project['status']) {
      case UPDATE_NOT_SECURE:
      case UPDATE_REVOKED:
        $entry['title'] .= ' ' . t('(Security update)');
        $entry['#weight'] = -2;
        $type = 'security';
        break;

      case UPDATE_NOT_SUPPORTED:
        $type = 'unsupported';
        $entry['title'] .= ' ' . t('(Unsupported)');
        $entry['#weight'] = -1;
        break;

      case UPDATE_UNKNOWN:
      case UPDATE_NOT_FETCHED:
      case UPDATE_NOT_CHECKED:
      case UPDATE_NOT_CURRENT:
        $type = 'recommended';
        break;

      default:
        // Jump out of the switch and onto the next project in foreach.
        continue 2;
    }

    $entry['#attributes'] = array('class' => array('update-' . $type));

    // Drupal core needs to be upgraded manually.
    $needs_manual = $project['project_type'] == 'core';

    if ($needs_manual) {
      // There are no checkboxes in the 'Manual updates' table so it will be
      // rendered by theme('table'), not theme('tableselect'). Since the data
      // formats are incompatible, we convert now to the format expected by
      // theme('table').
      unset($entry['#weight']);
      $attributes = $entry['#attributes'];
      unset($entry['#attributes']);
      $entry = array(
        'data' => $entry,
      ) + $attributes;
    }
    else {
      $form['project_downloads'][$name] = array(
        '#type' => 'value',
        '#value' => $recommended_release['download_link'],
      );
    }

    // Based on what kind of project this is, save the entry into the
    // appropriate subarray.
    switch ($project['project_type']) {
      case 'core':
        // Core needs manual updates at this time.
        $projects['manual'][$name] = $entry;
        break;

      case 'module':
      case 'theme':
        $projects['enabled'][$name] = $entry;
        break;

      case 'module-disabled':
      case 'theme-disabled':
        $projects['disabled'][$name] = $entry;
        break;
    }
  }

  if (empty($projects)) {
    $form['message'] = array(
      '#markup' => t('All of your projects are up to date.'),
    );
    return $form;
  }

  $headers = array(
    'title' => array(
      'data' => t('Name'),
      'class' => array('update-project-name'),
    ),
    'installed_version' => t('Installed version'),
    'recommended_version' => t('Recommended version'),
  );

  if (!empty($projects['enabled'])) {
    $form['projects'] = array(
      '#type' => 'tableselect',
      '#header' => $headers,
      '#options' => $projects['enabled'],
    );
    if (!empty($projects['disabled'])) {
      $form['projects']['#prefix'] = '<h2>' . t('Enabled') . '</h2>';
    }
  }

  if (!empty($projects['disabled'])) {
    $form['disabled_projects'] = array(
      '#type' => 'tableselect',
      '#header' => $headers,
      '#options' => $projects['disabled'],
      '#weight' => 1,
      '#prefix' => '<h2>' . t('Disabled') . '</h2>',
    );
  }

  // If either table has been printed yet, we need a submit button and to
  // validate the checkboxes.
  if (!empty($projects['enabled']) || !empty($projects['disabled'])) {
    $form['actions'] = array('#type' => 'actions');
    $form['actions']['submit'] = array(
      '#type' => 'submit',
      '#value' => t('Download these updates'),
    );
    $form['#validate'][] = 'update_manager_update_form_validate';
  }

  if (!empty($projects['manual'])) {
    $prefix = '<h2>' . t('Manual updates required') . '</h2>';
    $prefix .= '<p>' . t('Updates of Drupal core are not supported at this time.') . '</p>';
    $form['manual_updates'] = array(
      '#type' => 'markup',
      '#markup' => theme('table', array('header' => $headers, 'rows' => $projects['manual'])),
      '#prefix' => $prefix,
      '#weight' => 120,
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/update/update.manager.inc](https://github.com/drupal/drupal/blob/7.103/modules/update/update.manager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
