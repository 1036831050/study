void RvizVisualizer::PublishPolynomialCurve(SYS_GUARDRAIL_DICT* ptr_guardrail_dict_t)
{
  visualization_msgs::MarkerArray marker_array;
  visualization_msgs::Marker marker;
  marker.header.frame_id = "car";
  marker.header.stamp = ros::Time::now();
  marker.action = visualization_msgs::Marker::DELETEALL;
  marker_array.markers.push_back(marker);
  for (int i = 0; i < ptr_guardrail_dict_t->valid_num; i++)
  {
    if (ptr_guardrail_dict_t->list[i].FLAGS.flags.flg_valid == H_FALSE)
    {
        continue;
    }
    marker.ns = "polynomial_curve";
    marker.id = i;
    marker.type = visualization_msgs::Marker::LINE_STRIP;
    marker.action = visualization_msgs::Marker::ADD;
    marker.pose.orientation.w = 1.0;

  // 设置线条的颜色
    marker.color.r = 1.0;
    marker.color.g = 0.4313;
    marker.color.b = 0.7058;
    marker.color.a = 1.0;

    marker.scale.x = 0.3; // 线条宽度

    marker.points.clear();

  // 设置多项式曲线上的点
    for (float x = ptr_guardrail_dict_t->list[i].xmin; x <= ptr_guardrail_dict_t->list[i].xmax; x += 0.1)
    {
        geometry_msgs::Point p;
        p.x = x;
        p.y = ptr_guardrail_dict_t->list[i].curve[2] * x * x +  ptr_guardrail_dict_t->list[i].curve[1] * x + ptr_guardrail_dict_t->list[i].curve[0];
        p.z = 0;
        marker.points.push_back(p);
    }
    marker_array.markers.push_back(marker);
  }
  sys_guardrail_marker_pub.publish(marker_array);
}