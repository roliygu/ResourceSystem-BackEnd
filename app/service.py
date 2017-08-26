#! usr/bin/python
# coding=utf-8

from os.path import getsize

from .forms import LoginForm, UploadForm, TagCreateForm, ResourceEditForm
from .models import Resource, User, Tag
from .utils import save_file_storage, get_config, wrap_file_size
from .view_object import ValidateResult, UploadResult, TableCell, Table, ResourceHeader


class UserService:
    @staticmethod
    def validate_user(form: LoginForm, user: User):
        if form.username.data != get_config().username:
            return ValidateResult(False, "用户名错误")
        if not user.verify_password(form.password.data):
            return ValidateResult(False, "密码错误")
        return ValidateResult(True, "ok")


class ResourceService:
    @staticmethod
    def validate_upload(form: UploadForm):
        return ValidateResult(True, "ok")

    @staticmethod
    def upload_resource(form: UploadForm):
        resource = Resource()
        resource.name = form.name.data
        tags = TagService.search_tags_by_id(form.tag.data)
        resource.tags = tags
        file_storage = form.binary.data
        resource.origin_name = file_storage.filename
        resource.path = save_file_storage(file_storage)
        resource.size = getsize(resource.path)
        resource.insert()
        return UploadResult(True, "[{}]上传成功".format(resource.name))

    @staticmethod
    def get_resource(resource_id: int):
        return Resource.query.filter_by(id=resource_id).first()

    @staticmethod
    def delete_resource(resource: Resource):
        resource.delete()

    @staticmethod
    def update_resource(resource: Resource, form: ResourceEditForm):
        if form.name.data != resource.name:
            # todo 比较tag
            resource.name = form.name.data
            return resource.update()

    @staticmethod
    def scan_resources(limit=200):
        return Resource.query.limit(limit)

    @staticmethod
    def scan_resources_by_name(name: str):
        return Resource.get_all_by_name(name)

    @staticmethod
    def build_resource_table(resources: list, in_resource=False):
        row_list = []
        for row in resources:
            col_list = [TableCell(row.name), TableCell(row.origin_name),
                        # TableCell(row.path),
                        TableCell(wrap_file_size(row.size)), TableCell(row.create_time), TableCell(row.update_time),
                        TableCell(build_option_html(row.id, in_resource))]
            row_list.append(col_list)
        return Table(ResourceHeader, row_list)


class TagService:
    @staticmethod
    def add_tag(form: TagCreateForm):
        return Tag(name=form.name.data).insert()

    @staticmethod
    def search_tags_by_id(tags):
        return Tag.get_by_ids(set([int(item) for item in tags]))

    @staticmethod
    def scan_tag():
        return Tag.scan_tag()

    @staticmethod
    def get_tags_by_name(name: str):
        return Tag.get_by_name(name)

    @staticmethod
    def get_tag(tag_id: int):
        return Tag.query.filter_by(id=tag_id).first()

    @staticmethod
    def map_scan_tag():
        return [(str(tag.id), tag.name) for tag in TagService.scan_tag()]


option_html_template = """
<a href=\"resource/download/{}\"><span class=\"glyphicon glyphicon-save\" aria-hidden=\"true\"></span></a>&nbsp;&nbsp;
<a href=\"resource/delete/{}\"<span class=\"glyphicon glyphicon-remove\" aria-hidden=\"true\"></span></a>&nbsp;&nbsp;
<a href=\"resource/edit/{}\"<span class=\"glyphicon glyphicon-edit\" aria-hidden=\"true\"></span></a>
"""

resource_option_html_template = """
<a href=\"download/{}\"><span class=\"glyphicon glyphicon-save\" aria-hidden=\"true\"></span></a>&nbsp;&nbsp;
<a href=\"delete/{}\"<span class=\"glyphicon glyphicon-remove\" aria-hidden=\"true\"></span></a>&nbsp;&nbsp;
<a href=\"edit/{}\"<span class=\"glyphicon glyphicon-edit\" aria-hidden=\"true\"></span></a>
"""


def build_option_html(resource_id, in_resource):
    if in_resource:
        return resource_option_html_template.format(resource_id, resource_id, resource_id)
    else:
        return option_html_template.format(resource_id, resource_id, resource_id)
