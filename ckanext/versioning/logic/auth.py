# encoding: utf-8
from ckan.authz import is_authorized
from ckan.plugins import toolkit


def dataset_revert(context, data_dict):
    """Check if a user is allowed to revert a dataset to a version

    This is permitted only to users who are allowed to modify the dataset
    """
    return is_authorized('package_update', context,
                         {"id": data_dict['dataset']})


def dataset_tag_create(context, data_dict):
    """Check if a user is allowed to create a version

    This is permitted only to users who are allowed to modify the dataset
    """
    return is_authorized('package_update', context,
                         {"id": data_dict['dataset']})


def dataset_tag_delete(context, data_dict):
    """Check if a user is allowed to delete a version

    This is permitted only to users who are allowed to modify the dataset
    """
    return is_authorized('package_update', context,
                         {"id": data_dict['dataset']})


@toolkit.auth_allow_anonymous_access
def dataset_tag_list(context, data_dict):
    """Check if a user is allowed to list dataset versions

    This is permitted only to users who can view the dataset
    """
    return is_authorized('package_show', context, {"id": data_dict['dataset']})


@toolkit.auth_allow_anonymous_access
def dataset_tag_show(context, data_dict):
    """Check if a user is allowed to view dataset versions

    This is permitted only to users who can view the dataset
    """
    return is_authorized('package_show', context, {"id": data_dict['dataset']})


@toolkit.auth_allow_anonymous_access
def dataset_versions_diff(context, data_dict):
    return dataset_tag_show(context, data_dict)
